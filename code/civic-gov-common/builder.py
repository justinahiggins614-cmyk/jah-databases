#!/usr/bin/env python3
"""Shared builder for the civic/government database pairs
(government-agency-directory, land-records-cadastral,
public-infrastructure-assets, municipal-services, public-grants-funding,
humanitarian-disaster-relief - public + Signature editions).

Mirrors the recently-merged language-pashto pair structure:
  repo : db/<slug>/index.html + db/<slug>/gen-<slug>.js
  shard: data/<slug>/index.jsonl.gz + data/<slug>/chunks/chunk-0000.jsonl.gz
  frag : ~/workspace/hidden_files/missing-builds/fragments/<pair>.json

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.
Property of Justin Addam Higgins (JAH).
"""
import gzip
import importlib.util
import json
import os
import re
import subprocess
import sys

REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
FRAGDIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"
TEMPLATE_PAGE = os.path.join(REPO, "db", "language-pashto", "index.html")

sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate  # noqa: E402  (imports governance side effect)

BANNED = ["facebook", "bat belt"]
SIG_TAIL = ("Signature Civic Method, JAH system original. Labeled "
            "Signature-made; never presented as an authentic public record.")
RELIGIOUS = ["bible", "jesus", "allah", "muhammad", "moses", "buddha",
             "krishna", "prayer", "church", "mosque", "temple", "synagogue",
             "scripture", "divine", "gospel", "quran", "torah"]
PROFANE = ["fuck", "shit", "bitch", "bastard", "dick", "pussy", "cunt",
           "nigger", "faggot", "whore", "slut"]


def hdr(name, rid, group):
    return ("# Working demonstration for: %s\n"
            "# Record: %s | Group: %s\n"
            "# Real, runnable, stdlib-only Python. Prints real computed values,\n"
            "# asserts tight bounds, ends with the OK marker.\n"
            "NAME = %s\nRID = %s\nGROUP = %s\n"
            % (name, rid, group, json.dumps(name), json.dumps(rid),
               json.dumps(group)))


def _rep(text, old, new, slug, min_hits=1):
    n = text.count(old)
    if n < min_hits:
        raise AssertionError("template replacement missed in %s: %r" % (slug, old[:70]))
    return text.replace(old, new)


def render_page(slug, cfg):
    with open(TEMPLATE_PAGE, "r", encoding="utf-8") as f:
        t = f.read()
    t = _rep(t, "<title>The Pashto Language Database — JAH Databases</title>",
             "<title>%s — JAH Databases</title>" % cfg["name"], slug)
    t = _rep(t, "<h1>The Pashto Language Database</h1>",
             "<h1>%s</h1>" % cfg["name"], slug)
    # meta description + JSON-LD (same long text appears twice)
    old_desc = ("Learn Pashto from the ground up: the language overview, the "
                "44-letter Perso-Arabic alphabet, pronunciation and phonology, "
                "core vocabulary with sentences, grammar essentials, and themed "
                "sentence sets for daily life - every record carrying Pashto in "
                "Perso-Arabic script plus transliteration plus English translation "
                "plus example sentences, taught progressively along the ladder.")
    t = _rep(t, old_desc, cfg["meta_desc"], slug, 2)
    t = t.replace('"name": "The Pashto Language Database"',
                  '"name": %s' % json.dumps(cfg["name"]))
    # hero paragraph
    m = re.search(r"(<h1>.*?</h1>\s*<p>)(.*?)(</p>)", t, re.S)
    if not m:
        raise AssertionError("hero <p> not found in template")
    t = t[:m.start(2)] + cfg["hero_p"] + t[m.end(2):]
    # generator id (2 occurrences: stat + about card)
    t = _rep(t, "jahdb-language-pashto-1.0", "jahdb-%s-1.0" % slug, slug, 2)
    t = _rep(t, "Type: <b>Public records organized in the Signature system</b>",
             "Type: <b>%s</b>" % cfg["sig_type"], slug)
    t = _rep(t, "Search Pashto letters, words, verbs, tenses, phrases, grammar, dialogues...",
             cfg["search_ph"], slug)
    t = _rep(t, "JAH Pashto Language Archivist <button", "%s <button" % cfg["ai"], slug)
    t = _rep(t, 'placeholder="Ask about Pashto..."',
             'placeholder="%s"' % cfg["chat_ph"], slug)
    # about card
    m = re.search(r'(<dt>Archive</dt><dd>)(.*?)(</dd>)', t, re.S)
    t = t[:m.start(2)] + cfg["archive_blurb"] + t[m.end(2):]
    m = re.search(r'(<dt>Record schema</dt><dd class="mono">)(.*?)(</dd>)', t, re.S)
    t = t[:m.start(2)] + cfg["schema"] + t[m.end(2):]
    m = re.search(r'(<dt>Fields</dt><dd>)(.*?)(</dd>)', t, re.S)
    t = t[:m.start(2)] + cfg["fields"] + t[m.end(2):]
    m = re.search(r'(<dt>Generator</dt><dd>)(.*?)(</dd>)', t, re.S)
    t = t[:m.start(2)] + ("jahdb-%s-1.0 — %s" % (slug, cfg["gen_desc"])) + t[m.end(2):]
    m = re.search(r'(<dt>AI</dt><dd>)(.*?)(</dd>)', t, re.S)
    t = t[:m.start(2)] + ("%s — %s — and aware of the whole JAH Databases network "
                         "through cross-database reasoning. On-device Standard 1.0, "
                         "no key needed; uses the shared Signature backend "
                         "automatically when configured." % (cfg["ai"], cfg["role"])) + t[m.end(2):]
    m = re.search(r'(<dt>Signature system</dt><dd>)(.*?)(</dd>)', t, re.S)
    t = t[:m.start(2)] + ("%s. Property of Justin Addam Higgins (JAH)." % cfg["sig_type"]) + t[m.end(2):]
    t = _rep(t, "JAH Databases. Public records organized in the Signature system. "
                "Property of Justin Addam Higgins (JAH).",
             "JAH Databases. %s. Property of Justin Addam Higgins (JAH)." % cfg["sig_type"], slug)
    # gen pane description
    t = _rep(t, "Generate clearly-labeled Pashto language studies. Seeded archive "
                "records are the authoritative entries.", cfg["gen_desc"], slug)
    # script vars
    t = _rep(t, "var SLUG='language-pashto';", "var SLUG='%s';" % slug, slug)
    t = _rep(t, "data/language-pashto/", "data/%s/" % slug, slug)
    t = _rep(t, ("var db={slug:SLUG,name:'The Pashto Language Database',"
                 "ai_name:'JAH Pashto Language Archivist',"
                 "record_kind:'language learning record'};"),
             ("var db={slug:SLUG,name:%s,ai_name:%s,record_kind:%s};"
              % (json.dumps(cfg["name"]), json.dumps(cfg["ai"]),
                 json.dumps(cfg["record_kind"]))), slug)
    m = re.search(r"var ROLE='(.*?)';", t, re.S)
    if not m:
        raise AssertionError("ROLE not found in template")
    t = t[:m.start(1)] + cfg["role"].replace("\\", "\\\\").replace("'", "\\'") + t[m.end(1):]
    t = _rep(t, ("I am the JAH Pashto Language Archivist. Ask me about Pashto - from the "
                 "44-letter alphabet and sounds through core words, grammar, and "
                 "everyday sentences to stories, idioms, and conversations."),
             cfg["greet"], slug)
    t = _rep(t, "$('emblem').src=JAHDB.emblemSVG(db.name,'JAH-SI-');",
             "$('emblem').src=JAHDB.emblemSVG(db.name,%s);" % json.dumps(cfg["prefix"]), slug)
    # .kv grid: canon minmax(120px,1fr)
    t = _rep(t, ".kv{display:grid;grid-template-columns:minmax(96px,150px) minmax(120px,1fr)",
             ".kv{display:grid;grid-template-columns:minmax(120px,1fr) minmax(120px,1fr)", slug)
    # page-level content gates
    low = t.lower()
    for b in BANNED:
        assert b not in low, "banned phrase %r in page %s" % (b, slug)
    assert 'id="stCount"' in t and "var SLUG='%s';" % slug in t
    assert "minmax(120px,1fr)" in t and "pre.codeblock" in t
    assert "pill-ex" in t and "qmerge" in t, "Exhaustive pill / merger button missing"
    assert "dataset.p" in t, "tab-handler guard missing"
    return t


GEN_JS_TEMPLATE = r"""(function(){'use strict';
/* JAH %s generator — %s.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX=%s;
var FIELDS=%s;
var TOPICS=%s;
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# %s — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — %s',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A %s of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:%s,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:%s,generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(%s,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""


def render_gen_js(slug, cfg, topics_by_tier):
    js = GEN_JS_TEMPLATE % (
        cfg["name"], "jahdb-%s-1.0" % slug,
        json.dumps(cfg["prefix"]), json.dumps(cfg["gen_fields"]),
        json.dumps(topics_by_tier, ensure_ascii=False),
        cfg["demo_study_label"],
        cfg["record_kind"], cfg["record_kind"],
        json.dumps(cfg["gen_demo_kind"]),
        json.dumps("jahdb-%s-1.0" % slug),
        json.dumps(slug),
    )
    low = js.lower()
    for b in BANNED:
        assert b not in low, "banned phrase %r in gen-js %s" % (b, slug)
    return js


def write_shard_db(slug, recs):
    ddir = os.path.join(SHARD, "data", slug)
    cdir = os.path.join(ddir, "chunks")
    os.makedirs(cdir, exist_ok=True)
    with gzip.open(os.path.join(ddir, "index.jsonl.gz"), "wt", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps({"id": r["id"], "t": r["t"], "g": r["g"]},
                               ensure_ascii=False) + "\n")
    with gzip.open(os.path.join(cdir, "chunk-0000.jsonl.gz"), "wt", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    return len(recs)


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


def content_gate_blob(blob, rid):
    low = blob.lower()
    for b in BANNED:
        if b in low:
            raise AssertionError("banned phrase %r in %s" % (b, rid))
    for w in PROFANE:
        if re.search(r'\b%s\b' % w, low):
            raise AssertionError("profane word %r in %s" % (w, rid))
    for w in RELIGIOUS:
        if re.search(r'\b%s\b' % w, low):
            raise AssertionError("religious framing %r in %s" % (w, rid))


def build_records(slug, cfg, entries, demos, sig, gate):
    ordered = sorted(enumerate(entries), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        hits = [h for h in gate.check(slug, title) if h[0] != slug]
        if hits:
            raise AssertionError("dedupe gate refused %r (already in %s)" % (title, hits))
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            description = "Signature original interpretation. " + e["sig_lens"] + " " + e["description"]
            how = e["sig_lens"] + " " + e["how_it_works"]
            citations = list(e["citations"]) + [cfg["sig_citation_tail"]]
        else:
            description = e["description"]
            how = e["how_it_works"]
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description, "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"], "ladder_tier": e["ladder_tier"],
        }
        demo_fn = demos[e["demo_key"]]
        program = demo_fn(hdr, name if not sig else title, rid, e["group"], e["demo_data"])
        rec["demo"] = {"kind": "python", "language": "python", "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        content_gate_blob(json.dumps(rec), rid)
        gate.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def assert_records(slug, cfg, recs, sig):
    ids = [r["id"] for r in recs]
    assert len(ids) == len(set(ids)) == 34, "need exactly 34 unique ids in %s" % slug
    assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
    need = ("id", "t", "g", "name", "title", "description", "how_it_works",
            "key_points", "requirements", "standards", "citations",
            "src", "ladder_rank", "ladder_tier", "demo")
    for r in recs:
        for k in need:
            assert k in r, "missing %s in %s" % (k, r["id"])
        prog = r["demo"].get("program")
        assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
        assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
        assert r["ladder_tier"] in ("foundations", "compounded", "advanced")
        compile(prog, r["id"], "exec")
        if sig:
            assert "(signature edition)" in r["title"].lower()
            assert r["src"] == "signature"
        else:
            assert r["src"] == "public-harvest"


def run_demos(recs):
    for r in recs:
        p = subprocess.run([sys.executable, "-c", r["demo"]["program"]],
                           capture_output=True, text=True, timeout=180)
        assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
        assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]


def write_pages(slug, cfg, recs, sweep_path):
    page = render_page(slug, cfg)
    ddir = os.path.join(REPO, "db", slug)
    os.makedirs(ddir, exist_ok=True)
    ppath = os.path.join(ddir, "index.html")
    with open(ppath, "w", encoding="utf-8") as f:
        f.write(page)
    notes = []
    if sweep_path and os.path.exists(sweep_path):
        spec = importlib.util.spec_from_file_location("sweep_%s" % slug, sweep_path)
        sweep = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(sweep)
        _, notes = sweep.process_page(ppath)
        with open(ppath, "r", encoding="utf-8") as f:
            page = f.read()
    topics = {}
    for r in recs:
        topics.setdefault(r["g"], []).append(r["t"])
    gen_js = render_gen_js(slug, cfg, topics)
    gen_path = os.path.join(ddir, "gen-%s.js" % slug)
    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gen_js)
    scripts = _extract_scripts(page)
    assert scripts, "no inline scripts in %s" % slug
    for i, body in enumerate(scripts):
        chk = "/tmp/civic_%s_%d.js" % (slug.replace("-", "_"), i)
        with open(chk, "w", encoding="utf-8") as f:
            f.write(body)
        p = subprocess.run(["node", "--check", chk], capture_output=True,
                           text=True, timeout=60)
        assert p.returncode == 0, "page script %d failed node --check in %s: %s" % (
            i, slug, p.stderr[-500:])
    p = subprocess.run(["node", "--check", gen_path], capture_output=True,
                       text=True, timeout=60)
    assert p.returncode == 0, "gen js failed node --check in %s: %s" % (slug, p.stderr[-500:])
    print("  page: db/%s/index.html + gen-%s.js [%s] (js checked: %d page scripts + gen)"
          % (slug, slug, ", ".join(notes), len(scripts)), flush=True)


def write_fragment(pair_slug, pub_cfg, sig_cfg, pub_slug, sig_slug):
    def entry(slug, cfg, src):
        return {
            "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"], "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"], "record_count": 34, "status": "live",
            "full_records": 34, "source": src,
            "local_index": SHARD_BASE + "/data/%s/index.jsonl.gz" % slug,
            "index": SHARD_BASE + "/data/%s/index.jsonl.gz" % slug,
            "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % slug,
        }
    frag = {"public": entry(pub_slug, pub_cfg, "public-harvest"),
            "signature": entry(sig_slug, sig_cfg, "signature")}
    os.makedirs(FRAGDIR, exist_ok=True)
    path = os.path.join(FRAGDIR, pair_slug + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("  fragment: %s" % path, flush=True)


def run_pair(pair_slug, pub_slug, sig_slug, pub_cfg, sig_cfg, entries, demos):
    """Build one public+signature pair. ENTRIES shared; demos shared."""
    print("== %s / %s ==" % (pub_slug, sig_slug), flush=True)
    gate = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))
    demo_keys = {e["demo_key"] for e in entries}
    assert set(demos) == demo_keys, "demo map mismatch for %s: %s vs %s" % (
        pair_slug, set(demos), demo_keys)
    built = {}
    built[pub_slug] = build_records(pub_slug, pub_cfg, entries, demos, False, gate)
    built[sig_slug] = build_records(sig_slug, sig_cfg, entries, demos, True, gate)
    for slug, cfg, sig in ((pub_slug, pub_cfg, False), (sig_slug, sig_cfg, True)):
        assert_records(slug, cfg, built[slug], sig)
    for slug, recs in built.items():
        n = write_shard_db(slug, recs)
        print("  shard: %-38s %d records" % (slug, n), flush=True)
    for slug, recs in built.items():
        run_demos(recs)
    print("  demo execution: all %d demos ran OK" % sum(len(r) for r in built.values()),
          flush=True)
    sweep_path = ("/home/hatch/workspace/goals/database-quality-audit/hidden_files"
                  "/patches/sweep-db-pages.py")
    for slug, cfg, recs in ((pub_slug, pub_cfg, built[pub_slug]),
                            (sig_slug, sig_cfg, built[sig_slug])):
        write_pages(slug, cfg, recs, sweep_path)
    write_fragment(pair_slug, pub_cfg, sig_cfg, pub_slug, sig_slug)
    print("DONE: %s - 2 databases, 68 records. Merger handles manifest/api/restamp/commit."
          % pair_slug, flush=True)
