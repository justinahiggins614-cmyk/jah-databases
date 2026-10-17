#!/usr/bin/env python3
"""Build The Force and Motion Basics Database (fundamentals order #9).

Roster-verified 2026-10-17: slugs force-motion-basics /
force-motion-basics-signature free in the manifest; ID prefixes JAH-FMOB-
/ JAH-FMOBS- verified free in the manifest id_prefix values and in all 809
shard index files (zero hits); all 68 titles passed through
code/dedupe_gate.py against the whole system with zero refusals.

Two NEW databases, 34 ladder-ordered records each:

  force-motion-basics            - The Force and Motion Basics Database
                                   (public-harvest: real, fact-checked
                                   first-principles physics - push and pull,
                                   gravity, friction, speed and direction,
                                   and the simple machines: lever, wheel and
                                   axle, pulley, inclined plane, wedge, and
                                   screw; standard references Halliday
                                   Resnick Walker Fundamentals of Physics
                                   12th ed 2022; Serway and Jewett 10th ed
                                   2019; Young and Freedman University
                                   Physics 15th ed 2020; Hewitt Conceptual
                                   Physics 13th ed 2021; SI Brochure 9th ed;
                                   ISO 80000-3; ISO 80000-4; NIST SP 811;
                                   and the other landmarks cited per record)
  force-motion-basics-signature  - The Force and Motion Basics Signature
                                   Database
                                   (his original Signature Motion Method:
                                   every push a promise, every pull an
                                   agreement, gravity the Signature anchor,
                                   friction the Signature grip, and the
                                   simple machines the Signature leverage;
                                   src signature, titles suffixed
                                   " (Signature Edition)", never presented
                                   as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_force_motion_basics.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never runs git commit or
git push. A merger handles registration.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing on neutralizing or defeating military or
defense-grade systems.
"""
import importlib.util
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_force_motion_basics import ENTRIES, SIG_TAIL
from demos_force_motion_basics import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Motion "
                "Method: every push a promise, every pull an agreement, "
                "gravity the Signature anchor, friction the Signature grip, "
                "and the simple machines the Signature leverage. Clearly "
                "labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked first-principles "
                "physics: push and pull, gravity, friction, speed and "
                "direction, and the simple machines (lever, wheel and axle, "
                "pulley, inclined plane, wedge, screw) - every record "
                "carrying description, how it works, key points, "
                "requirements, standards, citations, and a working "
                "demonstration program, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what a force is, push and pull, position distance and "
              "displacement, speed, direction, velocity, acceleration, "
              "mass, weight, the newton, spring scales and force meters, "
              "balanced and unbalanced forces) -> Compounded (net force, "
              "free-body diagrams, Newton first second and third laws, "
              "gravity, friction, static and kinetic friction, air "
              "resistance and drag, momentum, the lever, the inclined "
              "plane) -> Advanced (the wheel and axle, the pulley, the "
              "wedge and the screw, mechanical advantage, work, energy, "
              "power, torque and rotational equilibrium, projectile "
              "motion, conservation of momentum in collisions).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search force, push and pull, gravity, friction, mass, weight, newtons, velocity, acceleration, momentum, lever, pulley, inclined plane, wedge, screw, work, energy, power, torque, projectiles, collisions...",
        "chat_ph": "Ask about force and motion...",
        "archive_blurb": ("Seeded %s force and motion basics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled force and motion basics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about force and motion - from what a force is through push and pull, position distance and displacement, speed, direction, velocity, acceleration, mass, weight, the newton, spring scales, and balanced and unbalanced forces, through net force, free-body diagrams, Newton three laws, gravity, friction, drag, momentum, the lever, and the inclined plane, to the wheel and axle, pulleys, wedge and screw, mechanical advantage, work, energy, power, torque, projectile motion, and collisions." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "force-motion-study", "gen_demo_kind": "force-motion-demo",
        "source": source,
    }

CIT_PUB = ("Force and motion physics (standard references: Halliday D, "
           "Resnick R, Walker J. Fundamentals of Physics. 12th ed. Wiley; "
           "2022; Serway RA, Jewett JW. Physics for Scientists and "
           "Engineers. 10th ed. Cengage; 2019; Young HD, Freedman RA. "
           "University Physics with Modern Physics. 15th ed. Pearson; "
           "2020; Hewitt PG. Conceptual Physics. 13th ed. Pearson; 2021; "
           "Knight RD. Physics for Scientists and Engineers: A Strategic "
           "Approach. 5th ed. Pearson; 2022; Cutnell JD, Johnson KW. "
           "Physics. 12th ed. Wiley; 2021; Giancoli DC. Physics: "
           "Principles with Applications. 8th ed. Pearson; 2020; Feynman "
           "RP, Leighton RB, Sands M. The Feynman Lectures on Physics. "
           "Vol. I; 1963; Bureau International des Poids et Mesures. The "
           "International System of Units (SI). 9th ed.; 2019; ISO "
           "80000-3:2019; ISO 80000-4:2019; NIST SP 811).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Motion Method - every push a promise, every pull an "
                     "agreement, gravity the Signature anchor - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["force-motion-basics"] = _cfg(
    "force-motion-basics", "The Force and Motion Basics Database",
    "Push and pull, gravity, friction, speed and direction, and the simple "
    "machines: real, fact-checked first-principles physics foundations, "
    "taught progressively from what a force is through Newton laws to "
    "projectile motion and collisions.",
    "force and motion basics record", "JAH-FMOB-", "JAH Force and Motion Basics Archivist",
    "force and motion basics archivist - teaching push and pull, gravity, "
    "friction, speed and direction, and the simple machines (lever, wheel "
    "and axle, pulley, inclined plane, wedge, screw); teaching progressively "
    "along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["force-motion-basics-signature"] = _cfg(
    "force-motion-basics-signature", "The Force and Motion Basics Signature Database",
    "His original Signature Motion Method: every push a promise, every pull "
    "an agreement, gravity the Signature anchor, friction the Signature "
    "grip, and the simple machines the Signature leverage. The full ladder "
    "from what a force is through Newton laws to projectile motion and "
    "collisions, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "force and motion basics record", "JAH-FMOBS-", "JAH Force and Motion Basics Archivist (Signature)",
    "force and motion basics archivist - Signature editions: his original "
    "Signature Motion Method, every push a promise and every pull an "
    "agreement, gravity the Signature anchor and the simple machines the "
    "Signature leverage, clearly labeled Signature-made and never presented "
    "as authentic public record; teaches progressively along the ladder "
    "from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + e["description"])
            how = e["sig_lens"] + " " + e["how_it_works"]
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = e["description"]
            how = e["how_it_works"]
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["key_points"], "; ".join(e["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def main():
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    built = {}
    for slug in ("force-motion-basics", "force-motion-basics-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) == 34, "expected 34 records in %s, got %d" % (slug, len(recs))
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                      "key_points", "requirements", "standards", "citations",
                      "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 10, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "universal build" not in page.lower(), "field leftover in %s" % slug
        assert "universal-build" not in page, "slug leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "universal build" not in gen_js.lower(), "field leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # NOTE: manifest.json / api.json registration is the merger's job -
    # this build deliberately does not touch them (concurrency rule).
    print("built %d databases, %d records total; manifest/api left for merger." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
