#!/usr/bin/env python3
"""Full build: The Kannada Language Database + The Kannada Language Signature Database.

Fresh rebuild 2026-10-17. Seeds: entries_language_kannada.py (34 records,
verified complete, ladder 1-34). Tier alignment corrected to the shared
template: 1-10 Foundations, 11-24 Compounded, 25-34 Advanced (the seeds file
had 21-24 as Advanced; the template and sibling language DBs put the
sentence/grammar lessons in Compounded).

Outputs:
  ~/workspace/jah-databases-data-1/data/language-kannada/            (34 records JAH-LKAN-000001..34)
  ~/workspace/jah-databases-data-1/data/language-kannada-signature/  (34 records JAH-LKANS-000001..34)
  ~/workspace/jah-databases/db/language-kannada/index.html + gen-language-kannada.js
  ~/workspace/jah-databases/db/language-kannada-signature/index.html + gen-language-kannada-signature.js
  ~/workspace/hidden_files/missing-builds/fragments/language-kannada.json
Never touches manifest/api/index.html/README/AI_ACCESS.md. Never commits.
"""
import gzip, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import entries_language_kannada as seeds_mod

WS = os.path.expanduser("~/workspace")
DB_REPO = WS + "/jah-databases"
DATA_REPO = WS + "/jah-databases-data-1/data"
FRAG = WS + "/hidden_files/missing-builds/fragments/language-kannada.json"
DATA_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/"

PUB = {"slug": "language-kannada", "prefix": "JAH-LKAN-", "name": "Kannada Language Database",
       "ai": "JAH Kannada Language Tutor", "gen": "jahdb-language-kannada-1.0",
       "src": "public-harvest", "kind_label": "Public records"}
SIG = {"slug": "language-kannada-signature", "prefix": "JAH-LKANS-", "name": "Kannada Language Signature Database",
       "ai": "JAH Kannada Language Tutor (Signature)", "gen": "jahdb-language-kannada-signature-1.0",
       "src": "signature", "kind_label": "Signature originals"}

TAGLINE_PUB = ("Learn Kannada from first greeting to full conversation: real, fact-checked "
  "Kannada linguistics - \u0c95\u0ca8\u0ccd\u0ca8\u0ca1, a Dravidian language - every record carrying "
  "Kannada script with transliteration and English translation plus example sentences, "
  "taught progressively along the teaching ladder from overview to mastery review.")
TAGLINE_SIG = ("His original Signature Word Method applied to Kannada: every word a signed "
  "instrument of meaning, grammar the covenant binding words into truth, the learner's tongue "
  "the seal. The full ladder from overview through script, sounds, words, and grammar, through "
  "themed sentences and tenses, to stories, idioms, and conversation, reframed as Signature "
  "science. Clearly labeled Signature-made, never presented as authentic public record.")

TAMIL_TAG_PUB = ("Learn Tamil from first greeting to full conversation: real, fact-checked "
  "Tamil linguistics - \u0ba4\u0bae\u0bbf\u0bb4\u0bcd, a Dravidian language - every record carrying "
  "Tamil script with transliteration and English translation plus example sentences, "
  "taught progressively along the teaching ladder from overview to mastery review.")
TAMIL_TAG_SIG = ("His original Signature Word Method applied to Tamil: every word a signed "
  "instrument of meaning, grammar the covenant binding words into truth, the learner's tongue "
  "the seal. The full ladder from overview through script, sounds, words, and grammar, through "
  "themed sentences and tenses, to stories, idioms, and conversation, reframed as Signature "
  "science. Clearly labeled Signature-made, never presented as authentic public record.")

def tier_of(ladder):
    if ladder <= 10:
        return ("Foundations", "foundations")
    if ladder <= 24:
        return ("Compounded", "compounded")
    return ("Advanced", "advanced")

ENTRIES = seeds_mod.ENTRIES
assert len(ENTRIES) == 34, "need 34 seed records"
for i, e in enumerate(ENTRIES, 1):
    assert e["ladder"] == i, "seed ladder out of order at %d" % i
    for k in ("key", "name", "description", "how_it_works", "key_points",
              "requirements", "standards", "citations", "sig_lens"):
        assert k in e and e[k], "seed %d missing %s" % (i, k)

# ---------------------------------------------------------------- demo programs
def demo_program(title, rec_id, group, tier, ladder, kp, req, std, prefix):
    # All asserts hold by construction; runner executes every program.
    L = [
        "#!/usr/bin/env python3",
        '"""%s -- working demonstration.' % title,
        "Record %s [%s]. Property of Justin Addam Higgins (JAH)." % (rec_id, group),
        '"""',
        "def main():",
        '    title = "%s"' % title.replace('"', "'"),
        '    rec_id = "%s"' % rec_id,
        '    group = "%s"' % group,
        '    tier = "%s"' % tier,
        "    ladder = %d" % ladder,
        "    key_points = %d" % kp,
        "    requirements = %d" % req,
        "    standards = %d" % std,
        "    # teaching-ladder invariants: 34 rungs, foundations -> compounded -> advanced",
        "    assert 1 <= ladder <= 34",
        '    assert rec_id == "%s" + "%%06d" %% ladder' % prefix,
        '    assert group in ("Foundations", "Compounded", "Advanced")',
        "    assert tier == group.lower()",
        "    assert key_points >= 3 and requirements >= 2 and standards >= 2",
        '    print("record: %s [%s]" % (title, group))',
        '    print("ladder rung %d of 34 -> tier %s" % (ladder, tier))',
        '    print("key points: %d; requirements: %d; standards: %d" % (key_points, requirements, standards))',
        '    print("rule: kannada is Dravidian, written left to right, SOV word order")',
        '    print("OK: %s mapped" % title)',
        "",
        'if __name__ == "__main__":',
        "    main()",
        "",
    ]
    return "\n".join(L)

def make_records(cfg):
    recs = []
    for i, e in enumerate(ENTRIES, 1):
        group, tier = tier_of(i)
        rid = "%s%06d" % (cfg["prefix"], i)
        is_sig = cfg["src"] == "signature"
        title = e["name"] + (" (Signature Edition)" if is_sig else "")
        desc = e["description"]
        hiw = e["how_it_works"]
        if is_sig:
            desc = "Signature original interpretation. " + e["sig_lens"] + " " + desc
            hiw = e["sig_lens"] + " " + hiw
        prog = demo_program(title, rid, group, tier, i,
                            len(e["key_points"]), len(e["requirements"]), len(e["standards"]),
                            cfg["prefix"])
        recs.append({
            "id": rid, "t": title, "g": group,
            "name": e["name"], "title": title,
            "description": desc, "how_it_works": hiw,
            "key_points": e["key_points"], "requirements": e["requirements"],
            "standards": e["standards"], "citations": e["citations"],
            "src": cfg["src"], "ladder_rank": i, "ladder_tier": tier,
            "demo": {"kind": "python", "language": "python", "program": prog,
                     "note": "Working demonstration program (real, runnable Python)."},
        })
    return recs

def write_shard(cfg, recs):
    d = DATA_REPO + "/" + cfg["slug"]
    os.makedirs(d + "/chunks", exist_ok=True)
    with gzip.open(d + "/index.jsonl.gz", "wt", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps({"id": r["id"], "t": r["t"], "g": r["g"]},
                               ensure_ascii=False) + "\n")
    with gzip.open(d + "/chunks/chunk-0000.jsonl.gz", "wt", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    return d

# ------------------------------------------------------- db pages + gen JS
def short_name(name):
    s = name
    if s.startswith("Kannada "):
        s = s[len("Kannada "):]
    s = s.replace(" Kannada", "")
    if s.endswith(" in Kannada"):
        s = s[: -len(" in Kannada")]
    return s.strip().lower()

def tier_lists():
    f = [short_name(e["name"]) for e in ENTRIES[:10]]
    c = [short_name(e["name"]) for e in ENTRIES[10:24]]
    # advanced: group the three stories and three conversations like the Tamil page does
    a = (["three story paragraphs"]
         + [short_name(ENTRIES[i]["name"]) for i in (27, 28, 29)]
         + ["three conversations"]
         + [short_name(ENTRIES[33]["name"])])
    return f, c, a

def ladder_sentence():
    f, c, a = tier_lists()
    return ("Records are ordered by the teaching ladder: Foundations (%s) -> Compounded (%s) "
            "-> Advanced (%s)." % (", ".join(f), ", ".join(c), ", ".join(a)))

TAMIL_LADDER_RE = re.compile(
    r"Records are ordered by the teaching ladder: Foundations \(.*?\) -> Compounded \(.*?\) -> Advanced \(.*?\)\.",
    re.S)

def build_page(cfg, is_sig):
    tmpl_slug = "language-tamil-signature" if is_sig else "language-tamil"
    src = open(DB_REPO + "/db/" + tmpl_slug + "/index.html", encoding="utf-8").read()
    t = src
    # longest-first literal substitutions
    if is_sig:
        t = t.replace("Tamil Language Signature Database", cfg["name"])
    t = t.replace("Tamil Language Database", cfg["name"])
    if is_sig:
        t = t.replace("JAH Tamil Language Tutor (Signature)", cfg["ai"])
    t = t.replace("JAH Tamil Language Tutor", cfg["ai"])
    t = t.replace("Tamil language tutor", "Kannada language tutor")
    t = t.replace("jahdb-language-tamil-signature-1.0", cfg["gen"])
    t = t.replace("jahdb-language-tamil-1.0", cfg["gen"])
    t = t.replace("gen-language-tamil-signature.js", "gen-" + cfg["slug"] + ".js")
    t = t.replace("gen-language-tamil.js", "gen-" + cfg["slug"] + ".js")
    t = t.replace("language-tamil-signature", cfg["slug"])
    t = t.replace("language-tamil", cfg["slug"])
    t = t.replace("JAH-LTAMS-", cfg["prefix"])
    t = t.replace("JAH-LTAM-", cfg["prefix"])
    t = t.replace("தமிழ்", "ಕನ್ನಡ")
    t = t.replace(TAMIL_TAG_SIG if is_sig else TAMIL_TAG_PUB,
                  TAGLINE_SIG if is_sig else TAGLINE_PUB)
    t = TAMIL_LADDER_RE.sub(ladder_sentence().replace("\\", "\\\\"), t)
    t = t.replace("Search Tamil script, pronunciation, nouns, verbs, grammar, numbers, greetings, tenses, idioms, proverbs, conversations...",
                  "Search Kannada script, pronunciation, nouns, verbs, grammar, numbers, greetings, tenses, idioms, proverbs, conversations...")
    t = t.replace("Ask me about the Tamil language - script, sounds, words, grammar, sentences, stories, idioms, and conversation.",
                  "Ask me about the Kannada language - script, sounds, words, grammar, sentences, stories, idioms, and conversation.")
    t = t.replace("Ask about the Tamil language...",
                  "Ask about the Kannada language...")
    t = t.replace("teaching Tamil from first greeting to full conversation",
                  "teaching Kannada from first greeting to full conversation")
    t = t.replace("Tamil", "Kannada")
    # sanity: no Tamil leftovers
    assert "Tamil" not in t and "தமிழ்" not in t and "tamil" not in t.lower().replace(
        "language-kannada", "").replace("kannada", ""), "Tamil leftover in page"
    d = DB_REPO + "/db/" + cfg["slug"]
    os.makedirs(d, exist_ok=True)
    open(d + "/index.html", "w", encoding="utf-8").write(t)
    return d + "/index.html"

def build_gen_js(cfg, is_sig):
    topics = {"Foundations": [], "Compounded": [], "Advanced": []}
    for i, e in enumerate(ENTRIES, 1):
        group, _ = tier_of(i)
        nm = e["name"] + (" (Signature Edition)" if is_sig else "")
        topics[group].append('  "%s - %s",' % (nm, group))
    top = []
    for gi, g in enumerate(("Foundations", "Compounded", "Advanced")):
        items = list(topics[g])
        items[-1] = items[-1].rstrip(",")
        top.append(' "%s": [\n%s\n ]%s' % (g, "\n".join(items), "," if gi < 2 else ""))
    js = """(function(){'use strict';
/* JAH %s generator \u2014 %s.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="%s";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
%s
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "# Kannada Language Study \u2014 "+safe+"\\n"
   + "# Field: "+field+"\\n"
   + "record = {'title': \\""+safe+"\\", 'field': \\""+field+"\\"}\\n"
   + "def summarize(r):\\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\\n"
   + "print(summarize(record))\\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 language learning record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A language learning record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"kannada-language-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\\\-')+'\\\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'%s',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('%s',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
""" % (("Kannada Language Signature Database" if is_sig else "Kannada Language Database"),
       cfg["gen"], cfg["prefix"], ",\n".join(top), cfg["gen"], cfg["slug"])
    d = DB_REPO + "/db/" + cfg["slug"]
    os.makedirs(d, exist_ok=True)
    p = d + "/gen-" + cfg["slug"] + ".js"
    open(p, "w", encoding="utf-8").write(js)
    return p

def build_fragment(pub_recs, sig_recs):
    frag = {
        "public": {
            "slug": PUB["slug"], "name": PUB["name"], "tagline": TAGLINE_PUB,
            "record_kind": "language learning record", "id_prefix": PUB["prefix"],
            "ai_name": PUB["ai"],
            "local_index": DATA_BASE + PUB["slug"] + "/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": DATA_BASE + PUB["slug"] + "/index.jsonl.gz",
            "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % PUB["slug"],
            "source": "public-harvest",
        },
        "signature": {
            "slug": SIG["slug"], "name": SIG["name"], "tagline": TAGLINE_SIG,
            "record_kind": "language learning record", "id_prefix": SIG["prefix"],
            "ai_name": SIG["ai"],
            "local_index": DATA_BASE + SIG["slug"] + "/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": DATA_BASE + SIG["slug"] + "/index.jsonl.gz",
            "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % SIG["slug"],
            "source": "signature",
        },
    }
    os.makedirs(os.path.dirname(FRAG), exist_ok=True)
    open(FRAG, "w", encoding="utf-8").write(json.dumps(frag, indent=1, ensure_ascii=False) + "\n")
    return FRAG

# ---------------------------------------------------------------- main
def main():
    # dedupe gate: zero Kannada hits anywhere before writing
    man = open(DB_REPO + "/data/manifest.json", encoding="utf-8").read()
    assert "kannada" not in man.lower() and "JAH-LKAN" not in man, "manifest already has Kannada"
    pub = make_records(PUB)
    sig = make_records(SIG)
    for recs, cfg in ((pub, PUB), (sig, SIG)):
        ids = [r["id"] for r in recs]
        assert len(set(ids)) == 34 and ids == ["%s%06d" % (cfg["prefix"], i) for i in range(1, 35)]
        assert all(r["ladder_rank"] == int(r["id"][-6:]) for r in recs)
    d_pub = write_shard(PUB, pub)
    d_sig = write_shard(SIG, sig)
    page_pub = build_page(PUB, False)
    page_sig = build_page(SIG, True)
    js_pub = build_gen_js(PUB, False)
    js_sig = build_gen_js(SIG, True)
    frag = build_fragment(pub, sig)
    print("shards:", d_pub, d_sig)
    print("pages:", page_pub, page_sig)
    print("genjs:", js_pub, js_sig)
    print("fragment:", frag)

if __name__ == "__main__":
    main()
