#!/usr/bin/env python3
"""Build the Baguazhang Combat databases for JAH Databases
(Manon's combat orders 2026-10-17, combat batch 4).

Terminology fact-checked 2026-10-17 against Wikipedia 'Baguazhang'
(founder Dong Haichuan 1797-1882, Hebei, originally 'Zhuanzhang'/Turning
Palm, taught in Beijing from about 1864, taught the first three palms -
Single Change, Double Change, Smooth Body - consistently and varied the
last five by student; famous students Yin Fu, Cheng Tinghua, Liang
Zhenpu; circle walking 'turning the circle' as the characteristic stance
and movement training, beginner circle six to twelve feet; crescent-shaped
deer horn knives unique to the style, wind and fire wheels, bagua sword,
bagua broadsword, staff, spear, cane, hook sword, judge's pen, straight
double-edged sword), New World Encyclopedia 'Baguazhang' (founding
account; one of the three principal internal arts alongside xingyiquan
and taijiquan), GW Media 'Ba Gua Zhang (Ba Gua Palm)' Kungfu Culture
(the eight palm sequence - Dan Huan/Single-change, Shuang
Huan/Double-change, Shun Shi/Go-along, Bei Shen/Back-body, Zhuan
Shen/Turn-around, Mo Shen/Body-grind, Fan Shen/Body-flip, Hui
Shen/Body-return - in succession with inexhaustible changes; Tang Ni Bu
muddy walk with the turn and lock in switching moves; palm techniques -
pushing, supporting, leading, moving, hooking, chopping, penetrating,
dodging, intercepting, sticking, following, cutting, smashing, twisting,
lifting, collapsing, tucking, bumping, exploring, flipping), USA Dojo
'About Ba Gua Zhang' (Liang Zhenpu school: Tang Ni Bu mud sliding step;
Koubu toe-in and Baibu toe-out for changing direction; Waibu outer foot
and Neibu inner foot; Tui Mo Zhang turning the millstone palm with index
finger and thumb forming an 'L', eight steps per revolution; Gai Mo Zhang
covering millstone palm as the deceptive overhead strike; Dan Huan Zhang
as block then strike before changing direction), ZhaobaoTaiji
'Baguazhang' (palm shapes - upward, downward, vertical, hugging,
piercing, chopping, lifting, picking, collapsing, bumping, tucking; the
proverb 'shaped like a swimming dragon, looks like a monkey guarding,
sits like a tiger, turns like an eagle'; scissor legs, buckle and
switch, avoid the straight and hit diagonally), FreedomMartialArt 'Bagua
Zhang' (guerrilla-style tactics, evasive footwork, rooting maintained
while in motion, striking from indirect angles, constant change), and
Hay JG. The Biomechanics of Sports Techniques. 4th ed. Prentice-Hall;
1993 (striking mechanics, lever arms, momentum).

Creates two NEW databases, 34 ladder-ordered records each:

  combat-baguazhang              - The Baguazhang Combat Database
                              (public-harvest: real, fact-checked
                              Baguazhang - the eight trigram palm: circle
                              walking foundations, the mud-wading step,
                              the eight palm changes in sequence, single
                              and double palm strikes, elbow and shoulder
                              techniques, deer-horn knife and straight
                              sword basics, applications - each record a
                              technique with HOW TO DO IT step-by-step
                              body mechanics, ladder-ordered from basics
                              to advanced; civilian traditional-art scope)
  combat-baguazhang-signature    - The Baguazhang Combat Signature Database
                              (his original Signature combat method: the
                              circle as the signature itself, every palm
                              change a covenant of the turn, the
                              mud-wading step the first covenant and
                              mastery the final signature; src
                              signature, titles suffixed " (Signature
                              Edition)", clearly labeled Signature-made,
                              never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBBGZ- (public) and JAH-CBBGZS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_baguazhang.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before writing
pages.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles those. Only db/combat-baguazhang*/, code/combat-baguazhang-build,
the shard data dirs, and the fragment file are written.

Never the words "bat belt" anywhere. No website references. No Facebook.

SCREENING: civilian traditional-art instruction only - nothing
hate-adjacent, profane, or inappropriate; no religious talk; nothing on
neutralizing or defeating military or defense-grade systems.
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
FRAGMENTS = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combat_baguazhang import ENTRIES, SIG_TAIL
from demos_combat_baguazhang import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature combat "
                "method: the circle as the signature itself, every palm "
                "change a covenant of the turn, the mud-wading step the "
                "first covenant and mastery the final signature. Clearly "
                "labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked Baguazhang, the eight "
                "trigram palm: circle walking foundations, the mud-wading "
                "step, swing and hook steps, posture and alignment, the "
                "eight static palm postures, the eight palm changes in "
                "sequence (single, double, flowing body, back-body, turning "
                "body, rubbing body, overturning body, returning body), "
                "single and double palm strikes, the millstone and covering "
                "millstone palms, the eight trigrams, elbow and shoulder "
                "techniques, palm strike variations, sticking and turning "
                "entries, deer-horn knives, the straight sword, spear and "
                "staff, swimming-body strategy, coiling power, the old "
                "eight palms form, side entries, the circle strategy "
                "against multiple attackers, and mastery - every record a "
                "technique with HOW TO DO IT step-by-step body mechanics, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what baguazhang means, circle walking, the mud-wading "
              "step, swing and hook steps, posture and alignment, the "
              "eight static palm postures, the single palm change, the "
              "double palm change, single palm strike mechanics, double "
              "palm strike mechanics, turning the millstone palm, breathing "
              "and relaxation) -> Compounded (flowing body palm, back-body "
              "palm, turning body palm, rubbing body palm, overturning body "
              "palm, returning body palm, covering millstone palm, the "
              "eight trigrams and the palms, elbow techniques, the shoulder "
              "strike, palm strike variations, sticking and turning "
              "entries) -> Advanced (deer-horn knife basics, deer-horn "
              "knife changes and trapping, straight sword basics, spear and "
              "staff, swimming-body strategy, coiling power, the old eight "
              "palms form, entering from the side, the circle strategy "
              "against multiple attackers, mastery of the advanced "
              "circle).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search circle walking, mud-wading step, swing step, hook step, postures, single palm change, double palm change, flowing body, back-body, turning body, rubbing body, overturning body, returning body, millstone palm, trigrams, elbows, shoulder strike, deer-horn knives, straight sword, spear, staff, coiling power, old eight palms...",
        "chat_ph": "Ask about baguazhang techniques...",
        "archive_blurb": ("Seeded %s baguazhang combat technique records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled baguazhang combat technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about baguazhang - from what the eight trigram palm means, circle walking, the mud-wading step, swing and hook steps, posture, the static postures, the single and double palm changes, single and double palm strikes, the millstone palm, and breathing, through the flowing body, back-body, turning body, rubbing body, overturning body, and returning body changes, the covering millstone, the eight trigrams, elbows, the shoulder strike, palm variations, and sticking entries, to deer-horn knives, the straight sword, spear and staff, swimming-body strategy, coiling power, the old eight palms form, side entries, the circle strategy, and mastery." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "baguazhang-combat-study", "gen_demo_kind": "baguazhang-combat-demo",
        "source": source,
    }

CIT_PUB = ("Baguazhang technique and tradition (standard references: "
           "Wikipedia, \"Baguazhang\" - founder Dong Haichuan 1797-1882, "
           "Hebei, originally 'Zhuanzhang'/Turning Palm, taught Beijing "
           "from about 1864, first three palms taught to every student, "
           "students Yin Fu, Cheng Tinghua, Liang Zhenpu; circle walking "
           "'turning the circle' as the characteristic training, beginner "
           "circle six to twelve feet; crescent-shaped deer horn knives "
           "unique to the style, wind and fire wheels, bagua sword, bagua "
           "broadsword, staff, spear, cane, hook sword, judge's pen, "
           "straight double-edged sword; accessed 2026-10-17; New World "
           "Encyclopedia, \"Baguazhang\" - founding account, one of the "
           "three principal internal arts; accessed 2026-10-17; GW Media, "
           "\"Ba Gua Zhang (Ba Gua Palm)\", Kungfu Culture - the eight "
           "palm sequence (single-change, double-change, go-along, "
           "back-body, turn-around, body-grind, body-flip, body-return), "
           "Tang Ni Bu muddy walk, palm techniques; accessed 2026-10-17; "
           "USA Dojo, \"About Ba Gua Zhang\" - Tang Ni Bu mud sliding step, "
           "Koubu toe-in and Baibu toe-out, Waibu/Neibu, Tui Mo Zhang "
           "turning the millstone palm, Gai Mo Zhang covering millstone "
           "palm, Dan Huan Zhang; accessed 2026-10-17; Hay JG. The "
           "Biomechanics of Sports Techniques. 4th ed. Prentice-Hall; "
           "1993 - striking mechanics, lever arms, momentum).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature combat "
                     "method - the circle as the signature itself, every "
                     "palm change a covenant of the turn - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["combat-baguazhang"] = _cfg(
    "combat-baguazhang", "The Baguazhang Combat Database",
    "Baguazhang, the eight trigram palm: real, fact-checked technique "
    "records - circle walking foundations, the mud-wading step, the eight "
    "palm changes in sequence, single and double palm strikes, elbow and "
    "shoulder techniques, deer-horn knife and straight sword basics, and "
    "applications - each record a technique with HOW TO DO IT step-by-step "
    "body mechanics, taught progressively along the ladder from basics to "
    "advanced.",
    "combat technique record", "JAH-CBBGZ-", "JAH Baguazhang Combat Archivist",
    "baguazhang combat archivist - the eight trigram palm: circle walking, "
    "mud-wading step, the eight palm changes, palm strikes, elbows, "
    "shoulders, deer-horn knives, the straight sword, and applications; "
    "teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
    CIT_PUB, "public")
DBCFG["combat-baguazhang-signature"] = _cfg(
    "combat-baguazhang-signature", "The Baguazhang Combat Signature Database",
    "His original Signature combat method: the circle as the signature "
    "itself, every palm change a covenant of the turn, the mud-wading step "
    "the first covenant and mastery the final signature. The full ladder "
    "from what baguazhang means through circle walking, the eight palm "
    "changes, strikes, weapons, and strategy, reframed as Signature "
    "science. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "combat technique record", "JAH-CBBGZS-", "JAH Baguazhang Combat Archivist (Signature)",
    "baguazhang combat archivist - Signature editions: his original Signature "
    "combat method, the circle as the signature itself and every palm "
    "change a covenant of the turn, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively "
    "along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from "
    "this system",
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
    assert p.returncode == 0, "node --check failed %s (%s): %s" % (label, path, p.stderr[-500:])
    return True


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
    for slug in ("combat-baguazhang", "combat-baguazhang-signature"):
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
        assert "baguazhang" in page.lower(), "field content missing in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        # node --check on extracted inline page scripts (skip JSON-LD data blocks)
        scripts = []
        for m in re.finditer(r"<script([^>]*)>(.*?)</script>", page, re.S | re.I):
            attrs, body = m.group(1), m.group(2)
            if "src=" in attrs.lower():
                continue
            tm = re.search(r'type\s*=\s*["\']([^"\']+)', attrs, re.I)
            if tm and "javascript" not in tm.group(1).lower() and "ecmascript" not in tm.group(1).lower() and "module" not in tm.group(1).lower():
                continue
            scripts.append(body)
        checked = 0
        for i, body in enumerate(scripts):
            if body.strip():
                with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
                    tf.write(body)
                    tfp = tf.name
                node_check(tfp, "%s inline script %d" % (slug, i))
                os.unlink(tfp)
                checked += 1
        print("page scripts node --check: %d inline scripts clean [%s]" % (checked, slug), flush=True)
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
        node_check(gpath, "gen-%s.js" % slug)
        print("page:  db/%s/index.html + gen-%s.js node --check clean [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # fragment for the merger (metadata only - merger owns manifest/api)
    os.makedirs(FRAGMENTS, exist_ok=True)
    frag = {}
    for key, slug in (("public", "combat-baguazhang"), ("signature", "combat-baguazhang-signature")):
        cfg = DBCFG[slug]
        idx_url = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        frag[key] = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": idx_url,
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": idx_url,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest" if key == "public" else "signature",
        }
    fpath = os.path.join(FRAGMENTS, "combat-baguazhang.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % fpath, flush=True)

    # CONCURRENCY: manifest/api.json/index.html/README/AI_ACCESS and git are
    # owned by the merger. This builder stops here.
    print("manifest + api.json: SKIPPED (merger-owned)")
    print("git commit/push: SKIPPED (merger-owned)")
    print("DONE: %d databases, %d records. NEXT: merger runs restamp + commit." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
