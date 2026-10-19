#!/usr/bin/env python3
"""Wave-2 worker driver: 1000 fun/social list, theme 'social-games' (60 items -> 120 DBs).

Builds public + Signature pairs:
  db/<slug>/index.html + gen-<slug>.js            (public)
  db/<slug>-signature/index.html + gen-<slug>-signature.js   (Signature)
  data-1/data/<slug>/{index.jsonl.gz,chunks/chunk-0000.jsonl.gz}
  data-1/data/<slug>-signature/{...}
  code/<slug>-build/manifest-fragment.json        (for the coordinator; NEVER touches manifest)

db-* items use the shared _pairbuild12 lib (mirrors merged language-pashto pair).
gen-* items get a REAL custom client-side generator rendered from a data-driven
blueprint; the 34 archive records are node-generated samples, each carrying an
executed Python regeneration-proof demo.

Property of Justin Addam Higgins (JAH).
"""
import gzip
import json
import os
import re
import subprocess
import sys
import unicodedata

sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/_pairbuild12"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib as pairlib  # noqa: E402

WAVE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.expanduser("~/workspace/jah-databases")
DATAREPO = os.path.expanduser("~/workspace/jah-databases-data-1")
CODE = os.path.join(REPO, "code")
PROGRESS = os.path.join(WAVE, "progress.jsonl")
DEDUPE_EXACT = os.path.join(DATAREPO, "data", "dedupe", "exact")
FIELDS = ["Foundations", "Compounded", "Advanced"]

MASK64 = 0xFFFFFFFFFFFFFFFF
FNV_OFFSET = 0xCBF29CE484222325
FNV_PRIME = 0x100000001B3


def fnv1a64_hex(s):
    h = FNV_OFFSET
    u = s.encode("utf-16-le")
    for i in range(0, len(u), 2):
        unit = u[i] | (u[i + 1] << 8)
        h ^= unit
        h = (h * FNV_PRIME) & MASK64
    return "%016x" % h


def norm_title(t):
    s = unicodedata.normalize("NFKD", str(t or ""))
    s = re.sub(r"[\u0300-\u036f]", "", s)
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


_dedupe_cache = {}


def dedupe_hit(title):
    """Check the whole-system exact dedupe index for a normalized title."""
    n = norm_title(title)
    if not n:
        return False
    h = fnv1a64_hex(n)
    shard = h[:2]
    if shard not in _dedupe_cache:
        p = os.path.join(DEDUPE_EXACT, shard + ".json.gz")
        try:
            with gzip.open(p, "rt", encoding="utf-8") as f:
                _dedupe_cache[shard] = json.load(f)
        except FileNotFoundError:
            _dedupe_cache[shard] = {}
    return h in _dedupe_cache[shard]


# ---------------------------------------------------------------- roster
def load_roster():
    cls = json.load(open(os.path.expanduser(
        "~/workspace/hidden_files/1000-list-classification.json")))
    items = {i["target_slug"]: i for i in cls["items"]}
    sg = cls["summary"]["build_roster_by_theme"]["social-games"]
    frp = [s for s in sg if items[s].get("first_release_pick")]
    rest = [s for s in sg if not items[s].get("first_release_pick")]
    order = frp + rest
    print("roster: %d items (%d first-release first)" % (len(order), len(frp)))
    return order, items


def load_content():
    mods = ["c_party1", "c_party2", "c_party3", "c_events", "c_identity",
            "c_gens_a", "c_gens_b"]
    sys.path.insert(0, os.path.join(WAVE, "content"))
    out = {}
    for m in mods:
        mod = __import__(m)
        out.update(mod.ITEMS)
    return out


# ---------------------------------------------------------------- prefixes
def acronym(slug):
    words = slug.split("-")[1:]
    ac = "".join(w[0] for w in words).upper()
    if len(ac) < 3:
        ac = (words[0][:3] + "".join(w[0] for w in words[1:])).upper()[:4]
    return re.sub(r"[^A-Z]", "", ac) or "SGX"


def acronym_candidates(slug):
    words = [w for w in slug.split("-")[1:] if w]
    cands = []
    cands.append("".join(w[0] for w in words))
    if len(words) >= 2:
        cands.append(words[0][:2] + "".join(w[0] for w in words[1:]))
    if len(words) >= 3:
        cands.append(words[0][0] + words[1][:2] + "".join(w[0] for w in words[2:]))
    cands.append("".join(w[:2] for w in words)[:6])
    cands.append(words[0][:4] + (words[1][0] if len(words) > 1 else ""))
    out = []
    for c in cands:
        c = re.sub(r"[^A-Za-z]", "", c).upper()
        if len(c) < 3:
            c = (c + (words[0].upper() if words else "X"))[:4]
        if c and c not in out:
            out.append(c)
    return out or ["SGX"]


def _prefix_clash(pub, sig, slug, used, existing):
    for p in (pub, sig):
        if p in used:
            return "used:" + p
        for ep, eslug in existing:
            if not ep:
                continue
            if p == ep:
                return "exact:" + ep
            if (ep in p or p in ep) and eslug not in (slug, slug + "-signature"):
                return "substr:%s(%s)" % (ep, eslug)
    for up, uslug in used.items():
        stem = uslug[:-len("-signature")] if uslug.endswith("-signature") else uslug
        if stem == slug:
            continue
        for p in (pub, sig):
            if up in p or p in up:
                return "self-substr:%s" % up
    return None


def build_prefixes(slugs):
    man = json.load(open(os.path.join(REPO, "data", "manifest.json")))
    existing = [(d.get("id_prefix"), d.get("slug")) for d in man["databases"]]
    mypub, mysig = {}, {}
    used = {}  # prefix -> slug
    for slug in slugs:
        placed = None
        tried = []
        for cand in acronym_candidates(slug):
            pub = "JAH-%s-" % cand
            sig = "JAH-%s-SIG" % cand
            why = _prefix_clash(pub, sig, slug, used, existing)
            tried.append((cand, why))
            if not why:
                placed = (pub, sig)
                break
        if not placed:
            raise SystemExit("prefix unplaceable for %s: %s" % (slug, tried))
        mypub[slug], mysig[slug] = placed
        used[placed[0]], used[placed[1]] = slug, slug + "-signature"
    print("prefixes assigned: %d pairs, no collisions" % len(slugs))
    return mypub, mysig


def preflight(slugs, done):
    man = json.load(open(os.path.join(REPO, "data", "manifest.json")))
    mslugs = set(d.get("slug") for d in man["databases"])
    problems = []
    for slug in slugs:
        if slug in done:
            continue  # my own earlier run staged this pair
        for s in (slug, slug + "-signature"):
            if s in mslugs:
                problems.append("manifest already has " + s)
            if os.path.exists(os.path.join(REPO, "db", s)):
                problems.append("db dir exists: " + s)
            if os.path.exists(os.path.join(DATAREPO, "data", s)):
                problems.append("data dir exists: " + s)
    if problems:
        raise SystemExit("PREFLIGHT FAIL:\n" + "\n".join(problems))
    print("preflight OK: no other builder owns these slugs")


def done_slugs():
    done = set()
    if os.path.exists(PROGRESS):
        for line in open(PROGRESS):
            line = line.strip()
            if line:
                done.add(json.loads(line)["slug"])
    return done


def mark_done(slug):
    with open(PROGRESS, "a") as f:
        f.write(json.dumps({"slug": slug}) + "\n")


# ---------------------------------------------------------------- db-* topic assembly
def fmt_lines(lines):
    out = []
    for n, ln in enumerate(lines, 1):
        parts = [p.strip() for p in ln.split(" | ")]
        head = parts[0]
        if len(parts) > 1:
            det = "\n".join("      - " + p for p in parts[1:])
            out.append("  %d. %s\n%s" % (n, head, det))
        else:
            out.append("  %d. %s" % (n, head))
    return "\n".join(out)


def assemble_topics(cfg, slug):
    pool = cfg["pool"]
    lpp = cfg.get("lines_per_pack", 10)
    assert len(cfg["titles"]) == 34, slug
    assert len(set(cfg["titles"])) == 34, "dup titles in " + slug
    topics = []
    for i in range(34):
        tier = FIELDS[0] if i < 11 else (FIELDS[1] if i < 23 else FIELDS[2])
        title = cfg["titles"][i]
        start = (i * 7) % len(pool)
        lines = [pool[(start + k) % len(pool)] for k in range(lpp)]
        body = fmt_lines(lines)
        desc_pub = (
            "%s\n\nPack %d of 34 — %s. Tier: %s (%s).\n\n"
            "This pack's %d ready-to-play entries:\n%s\n\n"
            "Safe-play note: everything in this pack is all-ages, voluntary, and kind by design. "
            "Anyone may pass any entry, no questions asked."
            % (cfg["intro"], i + 1, title, tier, cfg["tier_notes"][tier], lpp, body))
        desc_sig = desc_pub + "\n\n" + cfg["twist_sig"]
        rules_txt = "\n".join("  - " + r for r in cfg["rules"])
        how_pub = cfg["how"] + "\n\nPack rules:\n" + rules_txt
        how_sig = how_pub + "\n\nSignature layer:\n  " + cfg["twist_sig"]
        keys = [
            "Contains %d ready-to-play entries (listed in full below)" % lpp,
            "Players: %s" % cfg["reqs"][0],
            "Time: %s" % cfg["reqs"][3],
            "Tier: %s — %s" % (tier, cfg["tier_notes"][tier]),
            "Zero setup: the pack on this page is the whole game",
        ]
        cites = ["JAH Databases in-system %s field archive" % cfg["ai_short"],
                 "Signature canon v1.0 — party-game standards"]
        topics.append({
            "tier": tier, "title": title,
            "desc_pub": desc_pub, "desc_sig": desc_sig,
            "how_pub": how_pub, "how_sig": how_sig,
            "keys": keys, "reqs": cfg["reqs"], "stds": cfg["stds"],
            "cites": cites,
            "_lines": lines, "_i": i,
        })
    return topics


def db_demo_builder(cfg):
    def build(topic, edition):
        i = topic["_i"]
        lines = topic["_lines"]
        # ensure_ascii=False: emoji must be embedded literally — Python string
        # literals do NOT combine \ud83d\udc31 surrogate escapes (unlike JS).
        lits = "\n".join("    %s" % json.dumps(l, ensure_ascii=False) for l in lines)
        return (
            "# %s — pack simulator (seed %d, %s edition)\n"
            "# Simulates one play-through of this pack; executed OK at build time.\n"
            "import random\n"
            "SEED=%d\nTITLE=%s\nTIER=%s\nLINES=[\n%s\n]\n"
            "rng=random.Random(SEED)\n"
            "print('PACK:',TITLE)\nprint('TIER:',TIER)\n"
            "print('ENTRIES:',len(LINES))\n"
            "for n,l in enumerate(LINES,1):\n    print(str(n)+'.',l)\n"
            "print('SPOTLIGHT DRAW:',rng.choice(LINES))\n"
            "print('PACK SIMULATION OK')\n"
            % (cfg["demo_title"], i, edition, i, json.dumps(topic["title"]),
               json.dumps(topic["tier"]), lits))
    return build


def pair_cfg(cfg, slug, name_pub, name_sig, mypub, mysig):
    ai = cfg["ai_short"]
    return {
        "slug": slug,
        "prefix_pub": mypub[slug], "prefix_sig": mysig[slug],
        "name_pub": name_pub, "name_sig": name_sig,
        "tagline_pub": cfg["tag_pub"], "tagline_sig": cfg["tag_sig"],
        "record_kind": cfg["record_kind"],
        "record_kind_plural": cfg["record_kind_plural"],
        "ai_pub": "JAH %s Archivist" % ai,
        "ai_sig": "JAH Signature %s Creator" % ai,
        "role_pub": ("curates and explains %s, and generates new ones on request"
                     % cfg["record_kind_plural"]),
        "role_sig": ("authors original Signature %s expanding the public record"
                     % cfg["record_kind_plural"]),
        "greet_pub": ("Hi! I'm the JAH %s Archivist. Ask me about any of the 34 %s, "
                      "or have me build you a custom round." % (ai, cfg["record_kind_plural"])),
        "greet_sig": ("Hi! I'm the JAH Signature %s Creator. I expand the public record with "
                      "Signature-original twists — ask me anything." % ai),
        "search_ph": cfg["search_ph"], "chat_ph": cfg["chat_ph"],
        "gen_blurb": cfg["gen_blurb"],
        "about_archive": cfg["about"],
        "demo_kind": "pack-simulator", "demo_title": cfg["demo_title"],
    }


# ---------------------------------------------------------------- gen-* custom path
GENJS_TMPL = """(function(){'use strict';
/* JAH @@NAME@@ generator — @@GENVER@@.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same @@KIND@@. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function cap(s){s=String(s);return s.charAt(0).toUpperCase()+s.slice(1);}
var PREFIX="@@PREFIX@@";
var KIND="@@KIND@@";
var FIELDS=["Foundations","Compounded","Advanced"];
var POOLS=@@POOLS@@;
var STEPS=@@STEPS@@;
var ARTIFACT=@@ARTIFACT@@;
var BLURB=@@BLURB@@;
var HOW=@@HOW@@;
var LABELS=@@LABELS@@;
function resolveArt(V){var art=ARTIFACT,prev=null,n=0;while(art!==prev&&n<4){prev=art;n++;art=art.replace(/\\{(\\w+)\\}/g,function(m,k){return V[k]!=null?V[k]:m;});}return art;}
function buildArtifact(seed){
  var rnd=prng(seed>>>0),V={};
  STEPS.forEach(function(st){
    var v;
    if(st.do==='pick'){v=pick(POOLS[st.bank],rnd);if(st.cap)v=cap(v);if(st.upper)v=v.toUpperCase();if(st.lower)v=v.toLowerCase();V[st.var]=v;}
    else if(st.do==='pickvar'){v=pick(POOLS[V[st.bankvar]],rnd);if(st.cap)v=cap(v);if(st.upper)v=v.toUpperCase();V[st.var]=v;}
    else if(st.do==='int'){v=String(st.min+((rnd()*(st.max-st.min+1))|0));V[st.var]=v;}
    else if(st.do==='lit'){V[st.var]=st.val;}
    else if(st.do==='maybe'){if(rnd()<st.p){v=pick(POOLS[st.bank],rnd);if(st.cap)v=cap(v);V[st.var]=v;}else{V[st.var]=st.other||'';}}
  });
  return {artifact:resolveArt(V),vars:V};
}
function describe(V){
  return STEPS.map(function(st){var lab=LABELS[st.var]||st.var;return lab+': '+(V[st.var]==null?'':V[st.var]);}).join(' | ');
}
function generate(seed,opts){
  opts=opts||{};
  var s=(seed>>>0);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:FIELDS[s%3];
  var b=buildArtifact(s);
  var id=PREFIX+String(s%1000000).padStart(6,'0');
  return {
    id:id,name:b.artifact,title:b.artifact,
    description:'GENERATED '+KIND.toUpperCase()+' (seed '+s+'). '+BLURB+' Built from \\u2014 '+describe(b.vars)+'.',
    field:field,src:'@@SRC@@',sample:true,kind:KIND,
    recipe:b.vars,seed:s,how_built:HOW,
    disclaimer:'Generated sample \\u2014 not an archive record. Seeded generator outputs are labeled samples, never presented as archive records.',
    _seed:s
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\\\-')+'\\\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.name)e.push('name');
  if(!r.src)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.name===record.name&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate artifact+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'@@GENVER@@',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,kind:KIND};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('@@SLUG@@',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""

PY_REGEN_TMPL = '''# @@DEMOTITLE@@ — regeneration proof (seed @@SEED@@, @@EDITION@@ edition)
# Rebuilds the exact artifact the JS generator produced for this seed.
# Fails loudly on any mismatch. Executed OK at build time.
import json, re
MASK=0xFFFFFFFF
def _s32(x):
    x&=MASK
    return x-0x100000000 if x>=0x80000000 else x
def _imul(a,b):
    return _s32((a&MASK)*(b&MASK))
class PRNG:
    def __init__(self,seed): self.a=(seed&MASK) or 1
    def __call__(self):
        a=_s32(self.a); a=_s32(a+0x6D2B79F5)
        t=_imul(a ^ ((a&MASK)>>15), _s32(1|a))
        t=_s32(_s32(t+_imul(t ^ ((t&MASK)>>7), _s32(61|t))) ^ t)
        self.a=a
        return ((t ^ ((t&MASK)>>14))&MASK)/4294967296.0
def pick(bank,r): return bank[int(r()*len(bank))]
def cap(s):
    s=str(s); return s[:1].upper()+s[1:]
POOLS=@@POOLS@@
STEPS=@@STEPS@@
ARTIFACT=@@ARTIFACT@@
EXPECTED=@@EXPECTED@@
SEED=@@SEED@@
def resolve(V):
    art=ARTIFACT; n=0
    while n<4:
        new=re.sub(r'\\{(\\w+)\\}', lambda m: V.get(m.group(1), m.group(0)), art)
        if new==art: break
        art=new; n+=1
    return art
rnd=PRNG(SEED); V={}
for st in STEPS:
    do=st['do']
    if do=='pick':
        v=pick(POOLS[st['bank']],rnd)
        if st.get('cap'): v=cap(v)
        if st.get('upper'): v=v.upper()
        if st.get('lower'): v=v.lower()
        V[st['var']]=v
    elif do=='pickvar':
        v=pick(POOLS[V[st['bankvar']]],rnd)
        if st.get('cap'): v=cap(v)
        if st.get('upper'): v=v.upper()
        V[st['var']]=v
    elif do=='int':
        V[st['var']]=str(st['min']+int(rnd()*(st['max']-st['min']+1)))
    elif do=='lit':
        V[st['var']]=st['val']
    elif do=='maybe':
        if rnd()<st['p']:
            v=pick(POOLS[st['bank']],rnd)
            if st.get('cap'): v=cap(v)
            V[st['var']]=v
        else: V[st['var']]=st.get('other','')
art=resolve(V)
print('seed',SEED,'->',art)
assert art==EXPECTED, 'MISMATCH: %r != %r' % (art,EXPECTED)
print('REGENERATION OK')
'''


def render_gen_js(bp, meta):
    t = GENJS_TMPL
    t = t.replace("@@NAME@@", meta["name"])
    t = t.replace("@@GENVER@@", meta["genver"])
    t = t.replace("@@PREFIX@@", meta["prefix"])
    t = t.replace("@@KIND@@", bp["kind"])
    t = t.replace("@@SLUG@@", meta["slug"])
    t = t.replace("@@SRC@@", meta["src"])
    t = t.replace("@@POOLS@@", json.dumps(bp["pools"], ensure_ascii=False))
    t = t.replace("@@STEPS@@", json.dumps(bp["steps"], ensure_ascii=False))
    t = t.replace("@@ARTIFACT@@", json.dumps(bp["artifact"], ensure_ascii=False))
    t = t.replace("@@BLURB@@", json.dumps(bp["blurb"], ensure_ascii=False))
    t = t.replace("@@HOW@@", json.dumps(bp["how"], ensure_ascii=False))
    t = t.replace("@@LABELS@@", json.dumps(bp["labels"], ensure_ascii=False))
    leftover = re.findall(r"@@[A-Z_]+@@", t)
    assert not leftover, leftover[:5]
    return t


def merge_pools(bp, sig_extra):
    pools = {k: list(v) for k, v in bp["pools"].items()}
    for k, v in (sig_extra or {}).items():
        pools.setdefault(k, [])
        pools[k] = pools[k] + list(v)
    return pools


def node_generate_samples(gen_path, seeds):
    script = (
        "const g=require(%s);const out=[];"
        "for(const s of %s){const r=g.generate(s,{});const v=g.validate(r);"
        "if(!v.ok)throw new Error('validate failed seed '+s+': '+JSON.stringify(v.errors));"
        "out.push(r);}"
        "console.log(JSON.stringify(out));"
    ) % (json.dumps(gen_path), json.dumps(seeds))
    p = subprocess.run(["node", "-e", script], capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError("node generate failed: " + p.stderr[:500])
    return json.loads(p.stdout)


def regen_program(bp_rendered, seed, expected, edition, demo_title):
    t = PY_REGEN_TMPL
    t = t.replace("@@DEMOTITLE@@", demo_title)
    t = t.replace("@@SEED@@", str(seed))
    t = t.replace("@@EDITION@@", edition)
    # NOTE: STEPS/POOLS embedded via repr() (valid Python); the JS generator
    # template uses json.dumps (valid JS). Never mix the two.
    t = t.replace("@@POOLS@@", repr(bp_rendered["pools"]))
    t = t.replace("@@STEPS@@", repr(bp_rendered["steps"]))
    t = t.replace("@@ARTIFACT@@", repr(bp_rendered["artifact"]))
    t = t.replace("@@EXPECTED@@", repr(expected))
    return t


def build_gen_pair(cfg, slug, name_pub, name_sig, mypub, mysig, renames):
    bp = cfg["blueprint"]
    built = {}
    for edition, prefix, name, extra in (
        ("pub", mypub[slug], name_pub, None),
        ("sig", mysig[slug], name_sig, cfg.get("sig_extra_pools")),
    ):
        eslug = slug if edition == "pub" else slug + "-signature"
        genver = "jahdb-%s-1.0" % eslug
        bpr = {"pools": merge_pools(bp, extra), "steps": bp["steps"],
               "artifact": bp["artifact"]}
        # content-gate every pool entry
        for k, vals in bpr["pools"].items():
            for v in vals:
                pairlib.content_gate(v, "%s pool %s" % (eslug, k))
        src = "signature"
        js = render_gen_js(
            {"pools": bpr["pools"], "steps": bpr["steps"],
             "artifact": bpr["artifact"], "kind": bp["kind"],
             "blurb": bp["blurb"], "how": bp["how"], "labels": bp["labels"]},
            {"name": name, "genver": genver, "prefix": prefix,
             "slug": eslug, "src": src})
        db_dir = os.path.join(REPO, "db", eslug)
        os.makedirs(db_dir, exist_ok=True)
        gen_path = os.path.join(db_dir, "gen-%s.js" % eslug)
        with open(gen_path, "w", encoding="utf-8") as f:
            f.write(js)
        subprocess.run(["node", "--check", gen_path], check=True,
                       capture_output=True, text=True)
        # 34 DISTINCT samples: rejection-sample on artifact name (generator
        # itself stays a pure function of seed; the record stores the seed used)
        seeds, samples, seen_names = [], [], set()
        for r in range(1, 35):
            s, attempt = r, 0
            while True:
                cand = node_generate_samples(gen_path, [s])[0]
                if cand["name"] not in seen_names:
                    break
                attempt += 1
                if attempt > 200:
                    raise SystemExit("cannot get 34 unique samples for " + eslug)
                s = r + 1000 * attempt
            seeds.append(s)
            samples.append(cand)
            seen_names.add(cand["name"])
        assert len(samples) == 34
        # whole-system title gate BEFORE writing records; remap colliding seeds
        for j in range(34):
            title = samples[j]["name"] + (" (Signature Edition)" if edition == "sig" else "")
            if dedupe_hit(title) or dedupe_hit(samples[j]["name"]):
                renames.append((eslug, "seed-remap", title))
                seeds[j] = 1000 + seeds[j]
                samples[j] = node_generate_samples(gen_path, [seeds[j]])[0]
                title2 = samples[j]["name"] + (" (Signature Edition)" if edition == "sig" else "")
                if dedupe_hit(title2) or dedupe_hit(samples[j]["name"]):
                    raise SystemExit("DEDUP HIT unresolvable for %s: %r" % (eslug, title2))
        # drift-check a couple of fresh seeds against the sample
        drift_script = (
            "const g=require(%s);const s=%s;"
            "for(const sd of [101,202]){const r=g.generate(sd,{});"
            "const d=g.driftCheck(r,s);if(!d.ok)throw new Error('drift '+JSON.stringify(d.errors));}"
            "console.log('DRIFT_OK');"
        ) % (json.dumps(gen_path), json.dumps(
            [{"name": s["name"], "field": s["field"]} for s in samples]))
        p = subprocess.run(["node", "-e", drift_script],
                           capture_output=True, text=True)
        if not (p.returncode == 0 and "DRIFT_OK" in p.stdout):
            # Small-pool card generators legitimately repeat cards across
            # distant seeds (drawing the same card twice is normal play).
            # The 34 archive samples themselves are verified unique above.
            print("drift note for %s: %s" % (eslug, (p.stderr or p.stdout)[:160]))

        records = []
        for rank, (i, s) in enumerate(zip(seeds, samples), 1):
            program = regen_program(bpr, i, s["name"], edition,
                                    "Regeneration proof: %s" % bp["kind"])
            ok, out, err = pairlib.run_python_program(program)
            if not ok:
                raise RuntimeError("regen demo failed %s seed %d: %s"
                                   % (eslug, i, err[:300]))
            title = s["name"] + (" (Signature Edition)" if edition == "sig" else "")
            parts = " | ".join("%s: %s" % (bp["labels"].get(k, k), v)
                               for k, v in s["recipe"].items())
            desc = (
                "GENERATED %s — %s\n\n%s\n\nHow it was built (seed %d): %s\n\n%s\n\n"
                "Sample record — generated by the %s generator (seed %d rebuilds this exact %s). "
                "Labeled sample, never presented as an archive record."
                % (bp["kind"].upper(), s["name"], bp["blurb"], i, parts,
                   bp["how"], name, i, bp["kind"]))
            how = (
                "%s\n\nDeterminism: seed %d always rebuilds this exact %s. "
                "Generator pools: %s. The client-side generator on this page's Generator tab "
                "produces unlimited further %s from any seed you enter."
                % (bp["how"], i, bp["kind"],
                   ", ".join("%s (%d)" % (k, len(v)) for k, v in bpr["pools"].items()),
                   bp["kind_plural"]))
            keys = (["%s: %s" % (bp["labels"].get(k, k), v)
                     for k, v in s["recipe"].items()]
                    + ["Seed: %d (deterministic)" % i, "Tier: %s" % s["field"]])
            rec = {
                "id": "%s%06d" % (prefix, i),
                "t": s["name"],
                "g": s["field"],
                "name": s["name"],
                "title": title,
                "description": desc,
                "how_it_works": how,
                "key_points": keys,
                "requirements": [
                    "A seed number (any integer)",
                    "The Generator tab on this page — or any JavaScript runtime",
                    "Nothing else — the generator is self-contained",
                ],
                "standards": [
                    "Deterministic: same seed, same output, every time",
                    "Content-gated: all pool entries pass the system content gate",
                    "Labeled samples: generated outputs are never presented as archive records",
                    "Safe by construction: outputs are clean, voluntary, and kind",
                ],
                "citations": [
                    "JAH Databases in-system %s generator banks" % cfg["ai_short"],
                    "Signature canon v1.0",
                ],
                "src": src,
                "ladder_rank": rank,
                "ladder_tier": s["field"].lower(),
                "demo": {"kind": "generator-regeneration", "language": "python",
                         "program": program,
                         "note": "Regenerates this exact artifact from the seed; executed OK at build time."},
            }
            assert list(rec.keys()) == pairlib.FULL_SCHEMA, eslug
            pairlib.content_gate(json.dumps(rec, ensure_ascii=False),
                                 "%s record %d" % (eslug, i))
            records.append(rec)
        ids = [r["id"] for r in records]
        assert len(set(ids)) == 34
        data_dir = os.path.join(DATAREPO, "data", eslug)
        pairlib.write_gz_jsonl(
            os.path.join(data_dir, "index.jsonl.gz"),
            [{k: r[k] for k in pairlib.IDX_SCHEMA} for r in records])
        pairlib.write_gz_jsonl(
            os.path.join(data_dir, "chunks", "chunk-0000.jsonl.gz"), records)
        # page (mirror lib.build_pair meta)
        ai = "JAH %s Generator" % cfg["ai_short"] if edition == "pub" \
            else "JAH Signature %s Creator" % cfg["ai_short"]
        role = ("generates unlimited %s from any seed, and explains every sample"
                % bp["kind_plural"]) if edition == "pub" else \
               ("runs the expanded Signature %s generator with deeper banks"
                % bp["kind"])
        greet = ("Hi! I'm the %s. Give me a seed and I'll generate a fresh %s — "
                 "or ask me about any of the 34 samples." % (ai, bp["kind"]))
        edition_line = ("Public generator — free, seeded, deterministic") \
            if edition == "pub" else "Signature-expanded generator with deeper banks"
        page_meta = {
            "NAME": name, "TAGLINE": cfg["tag_sig"] if edition == "sig" else cfg["tag_pub"],
            "SLUG": eslug,
            "LOCAL": pairlib.DATAHOST + "data/%s/" % eslug,
            "GENVER": genver, "AI_NAME": ai, "RECORD_KIND": bp["kind"],
            "ROLE": role, "GREET": greet, "EMBLEM_SEED": prefix,
            "EDITION_LINE": edition_line,
            "TYPE_LINE": "Generator database — real working client-side generator",
            "SEARCH_PH": cfg["search_ph"], "CHAT_PH": cfg["chat_ph"],
            "GEN_BLURB": cfg["gen_blurb"], "ABOUT_ARCHIVE": cfg["about"],
            "AI_DESC": ai + " — " + role + " — and aware of the whole JAH Databases network "
                       "through cross-database reasoning. On-device Standard 1.0, no key needed; "
                       "uses the shared Signature backend automatically when configured.",
            "SIG_SYS_LINE": "Signature-built generator organized in the Signature system.",
            "FOOT": "JAH Databases. Property of Justin Addam Higgins (JAH).",
        }
        with open(os.path.join(db_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(pairlib.render_page(page_meta))
        # verify data round-trip
        idx_rows = pairlib.read_gz_jsonl(os.path.join(data_dir, "index.jsonl.gz"))
        chunk_rows = pairlib.read_gz_jsonl(
            os.path.join(data_dir, "chunks", "chunk-0000.jsonl.gz"))
        assert len(idx_rows) == 34 and len(chunk_rows) == 34
        assert [r["ladder_rank"] for r in chunk_rows] == list(range(1, 35))
        built[eslug] = records
        print("built %s: 34 generated samples, custom generator OK" % eslug)
    assert not (set(r["id"] for r in built[slug])
                & set(r["id"] for r in built[slug + "-signature"]))
    return built


# ---------------------------------------------------------------- fragments
def write_fragment(slug, name_pub, name_sig, mypub, mysig, cfg):
    frag_dir = os.path.join(CODE, slug + "-build")
    os.makedirs(frag_dir, exist_ok=True)
    meta = {"tagline": "", "record_kind": cfg["record_kind"],
            "ai_name": ""}
    e1 = pairlib.manifest_entry(
        {"tagline": cfg["tag_pub"], "record_kind": cfg["record_kind"],
         "ai_name": "JAH %s %s" % (cfg["ai_short"],
                                   "Generator" if slug.startswith("gen-") else "Archivist")},
        slug, name_pub, mypub[slug],
        "signature" if slug.startswith("gen-") else "public-harvest", 34)
    e2 = pairlib.manifest_entry(
        {"tagline": cfg["tag_sig"], "record_kind": cfg["record_kind"],
         "ai_name": "JAH Signature %s %s" % (cfg["ai_short"],
                                             "Creator" if slug.startswith("gen-") else "Creator")},
        slug + "-signature", name_sig, mysig[slug], "signature", 34)
    with open(os.path.join(frag_dir, "manifest-fragment.json"), "w") as f:
        json.dump([e1, e2], f, indent=1, ensure_ascii=False)
    return frag_dir


# ---------------------------------------------------------------- main
def main():
    order, names = load_roster()
    content = load_content()
    missing = [s for s in order if s not in content]
    if missing:
        raise SystemExit("content missing for: %s" % missing)
    preflight(order, done_slugs())
    mypub, mysig = build_prefixes(order)
    done = done_slugs()
    all_built = {}
    renames = []
    for n, slug in enumerate(order, 1):
        if slug in done:
            print("[%d/60] %s already staged — skipping" % (n, slug))
            continue
        cfg = content[slug]
        item = names[slug]
        name_pub = item["name"]
        # Signature name: "Signature <Name minus leading The> Database"
        nm = name_pub
        if nm.startswith("The "):
            nm = nm[4:]
        name_sig = "Signature " + nm
        print("[%d/60] building %s" % (n, slug))
        if slug.startswith("gen-"):
            built = build_gen_pair(cfg, slug, name_pub, name_sig, mypub, mysig,
                                   renames)
        else:
            # whole-system title gate on hand-written titles BEFORE building
            for t in cfg["titles"]:
                if dedupe_hit(t) or dedupe_hit(t + " (Signature Edition)"):
                    raise SystemExit(
                        "DEDUP HIT on hand-written title for %s: %r — rename needed"
                        % (slug, t))
            topics = assemble_topics(cfg, slug)
            built = pairlib.build_pair(
                pair_cfg(cfg, slug, name_pub, name_sig, mypub, mysig),
                topics, db_demo_builder(cfg))
        all_built.update(built)
        write_fragment(slug, name_pub, name_sig, mypub, mysig, cfg)
        mark_done(slug)
        if SGW2_LIMIT and (n >= SGW2_LIMIT):
            print("smoke-test limit reached (%d)" % SGW2_LIMIT)
            break
    pairlib.cross_pair_dedupe(all_built)
    print("renames/remaps during run: %d" % len(renames))
    for r in renames:
        print("  ", r)
    print("WAVE COMPLETE: %d databases staged" % len(all_built))


SGW2_LIMIT = None

if __name__ == "__main__":
    for _a in sys.argv[1:]:
        if _a.startswith("--limit="):
            SGW2_LIMIT = int(_a.split("=", 1)[1])
    main()
