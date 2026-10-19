#!/usr/bin/env python3
"""Build the eleven Decades databases for JAH Databases (time/history domain).

Gap audit 2026-10-18: no individual-decade database exists in the live
manifest (4,916 databases checked) - the 1920s through the 2020s were a
complete gap. This build creates 22 NEW databases, 34 ladder-ordered
records each (748 records):

  decades-1920s .. decades-2020s              (public-harvest: real,
      fact-checked landmark events, people, and turning points)
  decades-1920s-signature .. -signature       (Signature original
      interpretations - lessons, frameworks, builder's lenses; src
      signature, titles suffixed " (Signature Edition)", never
      presented as authentic public record)

34 records each, ladder-ordered 1-34 (foundations 1-10 / compounded
11-21 / advanced 22-34); the shard index is written in ladder order so
pages present simple -> compounded -> complex.

Demos: parametric date-math programs; expected values computed at build
time and embedded as literals; the build machine-executes all 748 demos.

Writes (this builder's scope ONLY - a merger handles the rest):
  main repo : db/decades-<D>/index.html + gen-decades-<D>.js (x22)
  shard repo: data/decades-<D>/index.jsonl.gz + chunks/chunk-0000.jsonl.gz (x22)
  build dir : code/decades-build/{build.py, entries_d*.py, demos_decades.py}
  fragment  : ~/workspace/hidden_files/missing-builds/fragments/decades-<D>.json (x11)

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.

No website references. No Facebook (except the Facebook record itself).
"""
import importlib.util
import json
import os
import pickle
import re
import subprocess
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGDIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"
CORPUS = "/home/hatch/workspace/hidden_files/govf2-title-corpus.pkl"

sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
from build_global_dedupe import norm_title
GATE = DedupeGate(os.path.join(SHARD, "data", "dedupe", "exact"))

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base

sys.path.insert(0, HERE)
from demos_decades import DEMOS, REF

with open(CORPUS, "rb") as f:
    TITLE_CORPUS = pickle.load(f)

SIG_TAIL = ("Signature editions are original Signature interpretations of the history, "
            "written as builder's lessons and frameworks. Signature-generated content is "
            "labeled as such and is never presented as authentic public record.")

CITATIONS = {
    "loc": "Library of Congress, manuscript and prints & photographs collections, Washington, DC.",
    "nara": "U.S. National Archives and Records Administration, record group holdings, Washington, DC.",
    "smithsonian": "Smithsonian Institution, National Museum of American History collections.",
    "nobel": "NobelPrize.org, Nobel Prize facts, biographies, and award citations.",
    "bbc": "BBC News and BBC History archives, contemporary reporting.",
    "nasa": "NASA History Division, historical publications and mission archives.",
    "ioc": "International Olympic Committee, Olympic Games results and historical archive.",
    "fbi": "Federal Bureau of Investigation, historical case files and records.",
    "metmuseum": "The Metropolitan Museum of Art, Egyptian Art collection archives.",
}

# (decade, short label, tagline, ai_pub, role_pub)
DECADES = [
 ("1920s", "the Roaring Twenties",
  "The Roaring Twenties: jazz, suffrage, Prohibition, Lindbergh, and the crash - the first modern decade, event by event.",
  "JAH 1920s Archivist",
  "1920s archivist - the Roaring Twenties: suffrage, Prohibition, radio, jazz, aviation firsts, and the 1929 crash; teaching progressively along the ladder from foundations through compounded to advanced"),
 ("1930s", "Depression and the drift to war",
  "Depression and the drift to war: the New Deal, the Dust Bowl, the rise of Hitler, and the inventions that endured.",
  "JAH 1930s Archivist",
  "1930s archivist - Depression and the drift to war: the New Deal, Dust Bowl, the rise of fascism, and the road to World War II; teaching progressively along the ladder from foundations through compounded to advanced"),
 ("1940s", "world war and the atomic age",
  "World war and the atomic age: the great battles, the Holocaust, the bomb, and the institutions built from the ruins.",
  "JAH 1940s Archivist",
  "1940s archivist - world war and the atomic age: the great battles, the Holocaust, Hiroshima, and the United Nations; teaching progressively along the ladder from foundations through compounded to advanced"),
 ("1950s", "boom, bomb, and the Cold War",
  "Boom, bomb, and the Cold War: suburbs and Sputnik, DNA and the Pill, the first victories of civil rights.",
  "JAH 1950s Archivist",
  "1950s archivist - boom, bomb, and the Cold War: the postwar boom, Korea, DNA, Sputnik, and the civil-rights movement; teaching progressively along the ladder from foundations through compounded to advanced"),
 ("1960s", "the decade that broke the mold",
  "The decade that broke the mold: civil rights, the Moon landing, Vietnam, and the assassinations that scarred it.",
  "JAH 1960s Archivist",
  "1960s archivist - the decade that broke the mold: civil rights, Apollo, Vietnam, the Beatles, and the assassinations; teaching progressively along the ladder from foundations through compounded to advanced"),
 ("1970s", "malaise and the microchip",
  "Malaise and the microchip: Watergate, the oil shocks, and the garage revolution that built the digital age.",
  "JAH 1970s Archivist",
  "1970s archivist - malaise and the microchip: Watergate, the end of Vietnam, the oil crisis, and the birth of personal computing; teaching progressively along the ladder from foundations through compounded to advanced"),
 ("1980s", "greed, gadgets, and the fall of the Wall",
  "Greed, gadgets, and the fall of the Wall: Reagan, the PC, MTV, and the Cold War's peaceful end.",
  "JAH 1980s Archivist",
  "1980s archivist - greed, gadgets, and the fall of the Wall: Reagan, the personal computer, MTV, and 1989; teaching progressively along the ladder from foundations through compounded to advanced"),
 ("1990s", "the end of history and the web",
  "The end of history and the web: the Soviet collapse, the Gulf War, and the internet's Cambrian explosion.",
  "JAH 1990s Archivist",
  "1990s archivist - the end of history and the web: the Soviet collapse, Mandela, the Gulf War, and the World Wide Web; teaching progressively along the ladder from foundations through compounded to advanced"),
 ("2000s", "9/11 and the networked age",
  "9/11 and the networked age: the towers, the wars, the iPhone, and the platforms that rewired humanity.",
  "JAH 2000s Archivist",
  "2000s archivist - 9/11 and the networked age: September 11, the wars, Wikipedia, the iPhone, and the 2008 crisis; teaching progressively along the ladder from foundations through compounded to advanced"),
 ("2010s", "the smartphone decade",
  "The smartphone decade: Instagram and the feed, the Higgs and CRISPR, and the movements that moved at share-speed.",
  "JAH 2010s Archivist",
  "2010s archivist - the smartphone decade: the iPad, Instagram, the Arab Spring, CRISPR, and the feed; teaching progressively along the ladder from foundations through compounded to advanced"),
 ("2020s", "the decade we're living",
  "The decade we're living: the pandemic, the wars, AI's arrival, and the polycrisis - history in real time.",
  "JAH 2020s Archivist",
  "2020s archivist - the decade we're living: COVID-19, the wars in Ukraine and Gaza, ChatGPT, and the climate crisis; teaching progressively along the ladder from foundations through compounded to advanced"),
]

ENTRIES_MOD = {
 "1920s": "entries_d1920", "1930s": "entries_d1930", "1940s": "entries_d1940",
 "1950s": "entries_d1950", "1960s": "entries_d1960", "1970s": "entries_d1970",
 "1980s": "entries_d1980", "1990s": "entries_d1990", "2000s": "entries_d2000",
 "2010s": "entries_d2010", "2020s": "entries_d2020",
}
ENTRIES_VAR = {
 "1920s": "E1920", "1930s": "E1930", "1940s": "E1940", "1950s": "E1950",
 "1960s": "E1960", "1970s": "E1970", "1980s": "E1980", "1990s": "E1990",
 "2000s": "E2000", "2010s": "E2010", "2020s": "E2020",
}

MONTHS = ["", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

# Minimal profanity/slur gate (legitimate historical vocabulary like war,
# bomb, kill, Nazi is NOT flagged - no false positives by design).
GATE_WORDS = ["fuck", "shit", "bitch", "cunt", "nigger", "faggot", "kike",
              "spic", "chink", "retard"]


def content_gate_ok(text, ctx):
    low = text.lower()
    for w in GATE_WORDS:
        if re.search(r"\b" + re.escape(w) + r"\b", low):
            return False, "banned word %r in %s" % (w, ctx)
    if "bat belt" in low:
        return False, "banned phrase in %s" % ctx
    return True, ""


def _cfg(dec, label, tagline, ai, role, source):
    # page template embeds ROLE in a single-quoted JS string with no escaping:
    # strip apostrophes from every config string that reaches JS/HTML contexts.
    role = role.replace("'", "")
    tagline = tagline.replace("'", "")
    ai = ai.replace("'", "")
    slug = "decades-%s%s" % (dec, "-signature" if source == "signature" else "")
    sig = source == "signature"
    dnum = dec.replace("s", "")
    prefix = "JAH-D%s%s-" % (dnum, "S" if sig else "")
    ai_name = ai + (" Signature" if sig else "")
    name = "The %s %sDatabase" % (dec, "Signature " if sig else "")
    pub_line = ("Public records - real, fact-checked landmark events, people, and turning points "
                "of %s, organized in the Signature system." % label)
    sig_line = ("Signature originals - original interpretations of %s as builder's lessons and "
                "frameworks, clearly labeled and never presented as authentic public record." % label)
    hero_p = ("%s - %s Every record carries the full entry: description, how it works, key points, "
              "requirements, standards, citations, and a working demonstration program. Records are ordered "
              "by the teaching ladder: Foundations (the decade at a glance and its defining moments) -> "
              "Compounded (landmark events and developments) -> Advanced (turning points, deep mechanisms, "
              "and consequences)." % (tagline, sig_line if sig else pub_line))
    return {
        "slug": slug, "name": name, "tagline": tagline,
        "record_kind": "%s history record" % dec,
        "prefix": prefix, "ai": ai_name, "role": role,
        "hero_p": hero_p,
        "sig_type": ("Signature originals organized in the Signature system"
                     if sig else "Public records organized in the Signature system"),
        "search_ph": "Search %s events, people, inventions, battles, elections..." % dec,
        "chat_ph": "Ask about the %s..." % dec,
        "archive_blurb": ("Seeded %s records of %s, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if sig else "public-record", label)),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations - Compounded - Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": ("Generate clearly-labeled %s studies. Seeded archive records are the authoritative entries." % dec),
        "greet": ("I am the %s. Ask me about %s - from the defining moments through the landmark events to the turning points and deep mechanisms." % (ai_name, label)),
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": dec, "gen_demo_kind": "decades-%s-demo" % dec,
        "source": source,
    }


DBCFG = {}
for _dec, _label, _tag, _ai, _role in DECADES:
    for _src in ("public", "signature"):
        _c = _cfg(_dec, _label, _tag, _ai, _role, _src)
        DBCFG[_c["slug"]] = _c
base.DBCFG = DBCFG


def load_entries(dec):
    mod = importlib.import_module(ENTRIES_MOD[dec])
    return list(getattr(mod, ENTRIES_VAR[dec]))


def _whole_system_hit(title):
    hx_hits = GATE.check("probe", title)
    if hx_hits:
        return hx_hits
    if norm_title(title) in TITLE_CORPUS:
        return [["shard-corpus", "?"]]
    return []


def build_records(slug, source, entries):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(entries), key=lambda p: (p[1]["rank"], p[0]))
    recs = []
    for _, e in ordered:
        # validate the anchor date is real
        ev = date(e["y"], e["m"], e["d"])
        assert ev <= REF, "anchor in the future: %s" % e["name"]
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        hits = _whole_system_hit(title)
        if hits:
            print("  gate refused (cross-db dupe): %s -> %s" % (title, hits[0][0]), flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        years = REF.year - ev.year - ((REF.month, REF.day) < (ev.month, ev.day))
        date_line = ("Anchor date: %s %d, %d - %d full years before the October 2026 reference date; "
                     "the day of the week was %s." % (MONTHS[ev.month], ev.day, ev.year, years, ev.strftime("%A")))
        if sig:
            description = "Signature original interpretation. " + e["sig_lens"] + " " + e["summary"]
            how = e["sig_lens"] + " " + e["mechanism"]
            citations = ["Encyclopaedia Britannica, s.v. \"%s,\" accessed October 2026." % e["ct"],
                         CITATIONS[e["c2"]], SIG_TAIL]
        else:
            description = e["summary"]
            how = e["mechanism"]
            citations = ["Encyclopaedia Britannica, s.v. \"%s,\" accessed October 2026." % e["ct"],
                         CITATIONS[e["c2"]]]
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": list(e["facts"]) + [date_line],
            "requirements": [
                "Pin the anchor date: %s %d, %d - every cause and consequence in this record hangs on it."
                % (MONTHS[ev.month], ev.day, ev.year),
                "Read one primary source from the time: a newspaper front page, a diary entry, a photograph, or an official record.",
                "Corroborate the headline facts across two independent accounts before repeating them.",
                "Place the event on the decade timeline: name what came right before and what came right after.",
                "Trace one consequence forward at least ten years to see what the event actually changed.",
            ],
            "standards": [
                "ISO 8601 date notation: the anchor date is %s." % ev.isoformat(),
                "Historical method: claims about the past are checked against contemporary evidence; later retellings are treated as secondary sources.",
            ],
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["rank"],
            "ladder_tier": e["tier"],
        }
        demo_data = {"y": ev.year, "m": ev.month, "d": ev.day, "rank": e["rank"],
                     "signature": sig}
        program = DEMOS["event"](title, rid, e["group"], demo_data)
        rec["demo"] = {"kind": "python", "language": "python", "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        GATE.admit(slug, title, rid)
        TITLE_CORPUS.add(norm_title(title))
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def _extract_scripts(page):
    scripts = []
    for m in re.finditer(r'<script([^>]*)>(.*?)</script>', page, re.S):
        attrs, body = m.group(1), m.group(2).strip()
        if re.search(r'\bsrc=', attrs):
            continue
        tm = re.search(r'type="([^"]+)"', attrs)
        if tm and tm.group(1) not in ("text/javascript", "application/javascript"):
            continue
        if body:
            scripts.append(body)
    return scripts


def main():
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
    order = []
    for dec, _, _, _, _ in DECADES:
        for source in ("public", "signature"):
            slug = "decades-%s%s" % (dec, "-signature" if source == "signature" else "")
            order.append(slug)
            entries = load_entries(dec)
            assert len(entries) == 34, "expected 34 entries for %s, got %d" % (dec, len(entries))
            built[slug] = build_records(slug, source, entries)
            print("records: %-32s %d" % (slug, len(built[slug])), flush=True)

    total = 0
    for slug in order:
        recs = built[slug]
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
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            ok, why = content_gate_ok(blob, r["id"])
            assert ok, why
            if "facebook.com" in blob:
                raise AssertionError("facebook.com URL outside its record in %s" % r["id"])
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-32s %d records" % (slug, n), flush=True)

    # execute every demo
    for slug in order:
        for r in built[slug]:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=120)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug in order:
        recs = built[slug]
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "facebook.com" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
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
        assert "facebook.com" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        gen_path = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gen_path, "w", encoding="utf-8") as f:
            f.write(gen_js)
        scripts = _extract_scripts(page)
        assert scripts, "no inline scripts found in %s" % slug
        for i, body in enumerate(scripts):
            chk = "/home/hatch/workspace/hidden_files/decades_check_%d.js" % i
            with open(chk, "w", encoding="utf-8") as f:
                f.write(body)
            p = subprocess.run(["node", "--check", chk],
                               capture_output=True, text=True, timeout=60)
            assert p.returncode == 0, "page script %d failed node --check in %s: %s" % (i, slug, p.stderr[-500:])
        p = subprocess.run(["node", "--check", gen_path],
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "gen js failed node --check in %s: %s" % (slug, p.stderr[-500:])
        print("page:  db/%s/index.html + gen-%s.js [%s] (js checked: %d page scripts + gen)"
              % (slug, slug, ", ".join(notes), len(scripts)), flush=True)

    for _d in os.listdir("/home/hatch/workspace/hidden_files"):
        if _d.startswith("decades_check_") and _d.endswith(".js"):
            os.remove(os.path.join("/home/hatch/workspace/hidden_files", _d))

    # fragments for the merger (manifest/api/restamp/commit)
    for dec, _, _, _, _ in DECADES:
        pub = "decades-%s" % dec
        sig = pub + "-signature"

        def frag_entry(slug, source):
            c = DBCFG[slug]
            return {
                "slug": slug, "name": c["name"], "tagline": c["tagline"],
                "record_kind": c["record_kind"], "id_prefix": c["prefix"],
                "ai_name": c["ai"], "local_index": SHARD_BASE + "/data/%s/index.jsonl.gz" % slug,
                "record_count": 34, "status": "staged", "full_records": 34,
                "index": SHARD_BASE + "/data/%s/index.jsonl.gz" % slug,
                "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % slug,
                "source": source,
            }

        fragment = {"public": frag_entry(pub, "public-harvest"),
                    "signature": frag_entry(sig, "signature")}
        os.makedirs(FRAGDIR, exist_ok=True)
        fpath = os.path.join(FRAGDIR, "%s.json" % pub)
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(fragment, f, indent=1, ensure_ascii=False)
            f.write("\n")
        print("fragment: %s" % fpath, flush=True)

    print("DONE: %d databases, %d records. Merger handles manifest/api/restamp/commit."
          % (len(order), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
