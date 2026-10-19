#!/usr/bin/env python3
"""Build the Pankration Combat databases for JAH Databases (combat batch 3).

Combat orders 2026-10-17, combat batch 3. Ancient Greek pankration: the
all-force art (pan = all, kratos = force) - Olympic history from 648 BC,
the two halves (pygme boxing, pale wrestling), stance, guard, footwork,
kicks, elbows, knees, throws, clinch, ground fighting, submissions
(klimax, strangles, joint locks), counters, strategy, the great
champions (Arrhichion, Sostratus, Dioxippus), and the modern revival.
Each record is a technique with HOW TO DO IT (step-by-step body
mechanics), ladder-ordered from foundations to advanced.

Dedupe 2026-10-17: all 68 titles checked against the WHOLE system via
code/dedupe_gate.py before authoring: zero collisions, zero refusals.
ID prefixes JAH-CBPK- / JAH-CBPKS- verified free in the manifest and in
every shard index (zero hits); combat-pankration slugs absent from
manifest.

So this build creates two NEW databases, 34 ladder-ordered records each:

  combat-pankration              - Pankration Combat Database
                                   (public-harvest: real, fact-checked
                                   ancient Greek pankration knowledge -
                                   Olympic history, pygme, pale, stance,
                                   guard, footwork, kicks, close strikes,
                                   throws, clinch, ground fighting,
                                   submissions, counters, strategy, the
                                   great champions, the modern revival -
                                   every record a technique with
                                   step-by-step body mechanics; standard
                                   references Philostratus Gymnasticus;
                                   Pausanias Description of Greece;
                                   Diodorus Siculus Library of History;
                                   Miller S.G. Arete 2004; Poliakoff M.B.
                                   Combat Sports in the Ancient World
                                   1987; Gardiner E.N. Athletics of the
                                   Ancient World 1930; World Pankration
                                   Athlima Federation competition rules;
                                   and the other landmarks cited per
                                   record)
  combat-pankration-signature    - Pankration Combat Signature Database
                                   (his original Signature Combat Method:
                                   every technique a covenant of
                                   discipline, the all-force fighter the
                                   armory of the Signature system, pan
                                   and kratos the two pillars of the oath,
                                   training the forge and the bout the
                                   proof; src signature, titles suffixed
                                   " (Signature Edition)", never
                                   presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_pankration.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Civilian martial-arts instruction only. Never the words "bat belt"
anywhere. No website references. No Facebook.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
It writes only db/combat-pankration[-signature]/,
code/combat-pankration-build/, and the shard data dirs. A merger handles
the manifest.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

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
from entries_combat_pankration import ENTRIES, SIG_TAIL
from demos_combat_pankration import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Combat "
                "Method: every technique a covenant of discipline, the "
                "all-force fighter the armory of the Signature system, pan "
                "and kratos the two pillars of the oath, training the "
                "forge and the bout the proof. Clearly labeled "
                "Signature-made, never presented as authentic public "
                "record.")
    pub_line = ("Public records - real, fact-checked ancient Greek "
                "pankration knowledge: Olympic history from 648 BC, the "
                "two halves (pygme boxing and pale wrestling), stance, "
                "guard, footwork, kicks (laktisma), close strikes (ankon, "
                "gony), throws (rhipsis, mesolabe), the clinch, ground "
                "fighting, submissions (klimax, apopnixis, joint locks), "
                "counters, strategy, the great champions, and the modern "
                "revival - every record a technique with step-by-step body "
                "mechanics, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(the all-force art, the parastasis stance, the cheires "
              "guard, footwork and measure, pygme, pale, the ancient "
              "prohibitions, falling and rolling, halteres conditioning, "
              "the skamma, breathing for the bout, the clinch tie-up) -> "
              "Compounded (the laktisma front kick, the turning kick, "
              "ankon elbows, gony knees, rhipsis throwing principles, the "
              "hip throw, the mesolabe waist lift, leg trips and foot "
              "sweeps, apopnixis the strangle, the top position, escapes "
              "from beneath, striking into the clinch) -> Advanced (the "
              "klimax ladder hold, trachelos chokes from behind, arm locks "
              "and joint control, counters, ground striking, the bout "
              "plan, the stand of Arrhichion, Sostratus the finger-"
              "fighter, Dioxippus against the armed soldier, the modern "
              "revival).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search pankration, parastasis, pygme, pale, laktisma, klimax, mesolabe, apopnixis, throws, clinch, submissions, stance, guard, footwork, Arrhichion, Sostratus, Dioxippus, revival...",
        "chat_ph": "Ask about pankration technique...",
        "archive_blurb": ("Seeded %s pankration combat records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled pankration technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about pankration - from the all-force art, the parastasis stance, the cheires guard, footwork and measure, pygme, pale, the ancient prohibitions, falling, halteres, the skamma, breathing, and the clinch tie-up, through the laktisma, turning kick, elbows, knees, rhipsis, hip throw, mesolabe, trips and sweeps, the strangle, top position, escapes, and striking into the clinch, to the klimax, chokes from behind, arm locks, counters, ground striking, the bout plan, Arrhichion, Sostratus, Dioxippus, and the modern revival." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "pankration-technique-study", "gen_demo_kind": "pankration-technique-demo",
        "source": source,
    }

CIT_PUB = ("Ancient Greek pankration history and technique (standard "
           "references: Philostratus. Gymnasticus (On Athletic Training), "
           "c. 3rd century AD; Pausanias. Description of Greece, 2nd "
           "century AD; Diodorus Siculus. Library of History 17.100-101; "
           "Miller S.G. Arete: Greek Sports from Ancient Sources. "
           "University of California Press; 2004; Poliakoff M.B. Combat "
           "Sports in the Ancient World. Yale University Press; 1987; "
           "Gardiner E.N. Athletics of the Ancient World. Oxford "
           "University Press; 1930; World Pankration Athlima Federation. "
           "Pankration Competition Rules and Technical Regulations; "
           "current edition).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Combat Method - every technique a covenant of "
                     "discipline, the all-force fighter the armory of the "
                     "Signature system - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["combat-pankration"] = _cfg(
    "combat-pankration", "Pankration Combat Database",
    "Ancient Greek all-force fighting taught step by step: Olympic "
    "history from 648 BC, the two halves of pygme and pale, stance, "
    "guard, footwork, kicks, close strikes, throws, the clinch, ground "
    "fighting, submissions, counters, strategy, the great champions, and "
    "the modern revival - every record a technique with how to do it, in "
    "plain body-mechanics language, ladder-ordered from foundations to "
    "advanced.",
    "combat technique record", "JAH-CBPK-", "JAH Pankration Combat Archivist",
    "pankration combat archivist - teaching ancient Greek all-force "
    "fighting step by step: Olympic history, pygme, pale, stance, guard, "
    "footwork, kicks, close strikes, throws, clinch, ground fighting, "
    "submissions, counters, strategy, the great champions, and the modern "
    "revival; teaching progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
    CIT_PUB, "public")
DBCFG["combat-pankration-signature"] = _cfg(
    "combat-pankration-signature", "Pankration Combat Signature Database",
    "His original Signature Combat Method: every technique a covenant of "
    "discipline, the all-force fighter the armory of the Signature "
    "system, pan and kratos the two pillars of the oath, training the "
    "forge and the bout the proof. The full ladder from the all-force "
    "art through stance, the two halves, kicks, throws, clinch, ground "
    "fighting, and submissions to counters, strategy, the champions, and "
    "the revival, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "combat technique record", "JAH-CBPKS-", "JAH Pankration Combat Archivist (Signature)",
    "pankration combat archivist - Signature editions: his original "
    "Signature Combat Method, every technique a covenant of discipline "
    "and the all-force fighter the armory of the Signature system, "
    "clearly labeled Signature-made and never presented as authentic "
    "public record; teaches progressively along the ladder from "
    "foundations through compounded to advanced; answers from many "
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


def node_check(path, label):
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True)
    assert p.returncode == 0, "node --check failed for %s: %s" % (label, p.stderr[-500:])


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
    for slug in ("combat-pankration", "combat-pankration-signature"):
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

    # cross-check entry text vs demo outputs: demo OK markers must name the record
    for slug, recs in built.items():
        for r in recs:
            p = subprocess.run([sys.executable, "-c", r["demo"]["program"]],
                               capture_output=True, text=True, timeout=60)
            ok_line = [l for l in p.stdout.splitlines() if l.startswith("OK:")]
            assert ok_line and r["name"] in ok_line[0], \
                "demo/text mismatch in %s: %s" % (r["id"], ok_line)

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
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        # JS hygiene: node --check the gen file and every inline page script
        node_check(gpath, "gen-%s.js" % slug)
        with open(ppath, "r", encoding="utf-8") as f:
            swept_page = f.read()
        scripts = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>",
                             swept_page, re.S | re.I)
        typed = re.findall(r"<script(?![^>]*\bsrc=)([^>]*)>",
                           swept_page, re.S | re.I)
        js_scripts = []
        for attrs, body in zip(typed, scripts):
            m = re.search(r'\btype\s*=\s*["\']([^"\']+)["\']', attrs, re.I)
            if m and "json" in m.group(1).lower():
                continue
            if m and not any(k in m.group(1).lower()
                             for k in ("javascript", "ecmascript", "module")):
                continue
            js_scripts.append(body)
        scripts = js_scripts
        for i, body in enumerate(scripts):
            if not body.strip():
                continue
            with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
                tf.write(body)
                tpath = tf.name
            try:
                node_check(tpath, "%s inline script %d" % (slug, i))
            finally:
                os.unlink(tpath)
        print("page:  db/%s/index.html + gen-%s.js [%s] [js: %d inline scripts node-clean]"
              % (slug, slug, ", ".join(notes), len(scripts)), flush=True)

    # NOTE (concurrency): manifest.json and api.json are owned by the merger.
    # This build does not touch them. Fragment for the merger is written by
    # the parent/orchestrator step; record counts for the fragment:
    for slug, recs in built.items():
        print("fragment-ready: %-38s %d records" % (slug, len(recs)), flush=True)
    print("NEXT: merger runs restamp + commit. This build committed nothing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
