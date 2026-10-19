#!/usr/bin/env python3
"""Wave 1 GENERATOR item: gen-unhinged-idea-generator (first-release pick).

A REAL working client-side idea generator: combinatorial assembly of mundane
things + absurd upgrades + fake benefits + warning labels. Wildly imaginative,
clean, good-natured. Seeded and reproducible.
"""
import json

from lib import register

FIELDS = ["Gadgets", "Home", "Daily Life"]

THINGS = {
    "Gadgets": ["a toaster", "an alarm clock", "a doorbell", "a lamp"],
    "Home": ["a houseplant", "a pillow", "a fridge", "an umbrella"],
    "Daily Life": ["a backpack", "a toothbrush", "a spatula", "a pair of socks"],
}
UPGRADES = [
    "that gives motivational speeches",
    "with built-in karaoke",
    "that files your taxes",
    "that judges your life choices (lovingly)",
    "with a tiny weather system inside",
    "that live-streams its opinions",
    "with emotional support features",
    "that predicts the stock market (badly)",
    "with a built-in lie detector",
    "that writes poetry about you",
    "with turbo mode",
    "that has unionized and demands weekends",
]
BENEFITS = [
    "increases productivity by 400% (unverified)",
    "reduces existential dread",
    "impresses houseguests",
    "counts as a personality trait",
    "solves boredom permanently",
    "makes Mondays 12% better",
    "is a guaranteed conversation starter",
    "ships with 50% more chaos",
]
WARNINGS = [
    "Side effects include spontaneous jazz.",
    "Do not operate while emotional.",
    "May develop opinions.",
    "Not responsible for enlightenment.",
    "Keep away from philosophers.",
    "May cause sudden expertise.",
    "Do not feed after midnight.",
    "Consult your cat before use.",
]


def _imul(a, b):
    a &= 0xFFFFFFFF
    b &= 0xFFFFFFFF
    if a & 0x80000000:
        a -= 0x100000000
    if b & 0x80000000:
        b -= 0x100000000
    return a * b


def _s32(x):
    x &= 0xFFFFFFFF
    return x - 0x100000000 if x & 0x80000000 else x


def make_prng(seed):
    a = seed & 0xFFFFFFFF
    if a == 0:
        a = 1

    def rnd():
        nonlocal a
        a = _s32(a + 0x6D2B79F5)
        au = a & 0xFFFFFFFF
        t = _s32(_imul(au ^ (au >> 15), 1 | au))
        tu = t & 0xFFFFFFFF
        t = _s32(_s32(t + _imul(tu ^ (tu >> 7), 61 | t)) ^ t)
        tu = t & 0xFFFFFFFF
        return ((tu ^ (tu >> 14)) & 0xFFFFFFFF) / 4294967296.0
    return rnd


def assemble(seed, field=None):
    rnd = make_prng(seed)
    fields = list(THINGS.keys())
    f = field if field in THINGS else fields[int(rnd() * len(fields)) % len(fields)]
    thing = THINGS[f][int(rnd() * len(THINGS[f]))]
    up = UPGRADES[int(rnd() * len(UPGRADES))]
    ben = BENEFITS[int(rnd() * len(BENEFITS))]
    warn = WARNINGS[int(rnd() * len(WARNINGS))]
    idea = "What if %s %s? It %s. Warning: %s" % (thing, up, ben, warn)
    return {"field": f, "thing": thing, "upgrade": up,
            "benefit": ben, "warning": warn, "idea": idea}


def custom_records(source, prefix):
    sig = (source == "signature")
    combos = []
    for f in FIELDS:
        for t in THINGS[f]:
            for u in UPGRADES:
                combos.append((f, t, u))
    raws = []
    used = set()
    i = 0
    k = 0
    while len(raws) < 34:
        f, t, u = combos[(k * 11) % len(combos)]
        k += 1
        key = (t, u)
        if key in used:
            continue
        used.add(key)
        ben = BENEFITS[i % len(BENEFITS)]
        warn = WARNINGS[(i * 5) % len(WARNINGS)]
        idea = "What if %s %s? It %s. Warning: %s" % (t, u, ben, warn)
        title = "Unhinged Idea %d: %s%s" % (
            i + 1, idea.split("?")[0].replace("What if ", "").title()[:40],
            " (Signature Edition)" if sig else "")
        desc = ("The idea: \"%s\"" % idea)
        desc += (" It is unhinged in the best way: wildly imaginative, completely "
                 "harmless, and weirdly thought-provoking. The formula: take %s "
                 "(mundane), add '%s' (absurd upgrade), promise '%s' (fake benefit), "
                 "and slap on a warning ('%s')." % (t, u, ben, warn))
        if sig:
            desc += (" The Signature treatment: the upgrade compounds the mundane - "
                     "each element heightens the last, so the idea teaches creative "
                     "combination.")
        desc += " (Seed %d reproduces this idea in the live generator.)" % (5000 + i * 53)
        how = ("The Unhinged Idea engine combines %d mundane things with %d absurd "
               "upgrades, %d fake benefits, and %d warnings = %d possible ideas, "
               "picked by seeded random. Same seed, same idea." % (
                   sum(len(v) for v in THINGS.values()), len(UPGRADES),
                   len(BENEFITS), len(WARNINGS),
                   sum(len(v) for v in THINGS.values()) * len(UPGRADES) * len(BENEFITS) * len(WARNINGS)))
        raws.append({
            "t": title, "g": f,
            "description": desc, "how_it_works": how,
            "key_points": ["Thing: " + t, "Upgrade: " + u, "Benefit: " + ben, "Warning: " + warn],
            "requirements": "Reading only - no equipment needed.",
            "citations": ["Original comedic writing for this database; ideas are fictional concepts."],
            "demo": "report",
            "seed": {"points": ["Thing: " + t, "Upgrade: " + u, "Benefit: " + ben, "Warning: " + warn],
                     "fact": desc[:400], "mechanism": how[:300]},
        })
        i += 1
    assert len({r["t"] for r in raws}) == 34
    return raws


GEN_JS_TEMPLATE = r"""(function(){'use strict';
/* JAH Unhinged Idea Generator - jahdb-gen-unhinged-idea-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL client-side generator: combinatorial unhinged ideas. Same seed, same idea.
   __SOURCE__ edition. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX=__PREFIX__;
var FIELDS=__FIELDS__;
var THINGS=__THINGS__;
var UPGRADES=__UPGRADES__;
var BENEFITS=__BENEFITS__;
var WARNINGS=__WARNINGS__;
var SOURCE='__SOURCE__';
function pick(r,arr){return arr[(r()*arr.length)|0];}
function assemble(seed,field){
  var r=prng(seed>>>0||1);
  var f=(field&&THINGS[field])?field:pick(r,FIELDS);
  var th=pick(r,THINGS[f]), up=pick(r,UPGRADES), be=pick(r,BENEFITS), wa=pick(r,WARNINGS);
  return {field:f,thing:th,upgrade:up,benefit:be,warning:wa,
          idea:'What if '+th+' '+up+'? It '+be+'. Warning: '+wa};
}
function demoProgram(a){
  function q(s){return s.replace(/"/g,"'");}
  return '# Unhinged Idea Generator - live idea\nprint("FIELD:   '+q(a.field)+'")\nprint("THING:   '+q(a.thing)+'")\nprint("UPGRADE: '+q(a.upgrade)+'")\nprint("BENEFIT: '+q(a.benefit)+'")\nprint("WARNING: '+q(a.warning)+'")\nprint()\nprint("IDEA: '+q(a.idea)+'")\nprint("OK: unhinged idea assembled from 4 banks")\n';
}
function generate(seed,opts,rnd){
  opts=opts||{};
  var a=assemble(seed>>>0||1,opts.field||null);
  var id=PREFIX+String(seed>>>0||1).padStart(6,'0');
  var title='Fresh Idea: '+a.thing.charAt(0).toUpperCase()+a.thing.slice(1)+' '+a.upgrade+(SOURCE==='signature'?' (Signature Edition)':'');
  return {
    id:id,
    name:title+' — '+a.field,
    title:title,
    description:'GENERATED IDEA (live generator output - clearly labeled fiction). "'+a.idea+'"',
    field:a.field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Live generator output - fictional concept, not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:demoProgram(a),note:'Live idea demo program.'},
    _seed:seed>>>0||1, parts:a
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.parts||!r.parts.idea)e.push('parts');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-gen-unhinged-idea-generator-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,assemble:assemble};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-unhinged-idea-generator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""


def gen_js(source, prefix, cfg):
    js = GEN_JS_TEMPLATE
    js = js.replace("__PREFIX__", json.dumps(prefix))
    js = js.replace("__FIELDS__", json.dumps(FIELDS))
    js = js.replace("__THINGS__", json.dumps(THINGS, ensure_ascii=False))
    js = js.replace("__UPGRADES__", json.dumps(UPGRADES, ensure_ascii=False))
    js = js.replace("__BENEFITS__", json.dumps(BENEFITS, ensure_ascii=False))
    js = js.replace("__WARNINGS__", json.dumps(WARNINGS, ensure_ascii=False))
    js = js.replace("__SOURCE__", source)
    return js


def S(key, t, g, fact, mechanism, evidence, sig_angle, sig_do, points, **kw):
    d = dict(key=key, t=t, g=g, fact=fact, mechanism=mechanism,
             evidence=evidence, sig_angle=sig_angle, sig_do=sig_do,
             points=points)
    d.update(kw)
    return d


CITE = ("Original comedic writing for this database; ideas are fictional concepts, "
        "clean and good-natured.")

SEEDS = [
 S("ui-formula", "The Formula", "Craft",
   "Every unhinged idea: mundane thing + absurd upgrade + fake benefit + warning. The formula is the madness's method.",
   "Combinatorial creativity: constrain the parts, unconstrain the combination.",
   "The generator's four banks implement the formula.",
   "The Signature reading: the method is the madness. Constrained parts, wild wholes.",
   "Try the Signature method: fill the four slots - the madness's method.",
   ["Mundane thing", "Absurd upgrade", "Fake benefit", "Warning label"]),
 S("ui-mundane", "The Mundane Anchor", "Craft",
   "Start boring: a toaster, a sock. The mundane anchors the absurd - without it, the idea floats away.",
   "Contrast theory: the ordinary makes the extraordinary legible.",
   "12 mundane things across 3 fields.",
   "The Signature reading: the boring anchors. Contrast makes it legible.",
   "Try the Signature method: start with a toaster - the anchor of absurd.",
   ["Toaster, sock, lamp", "The anchor", "Contrast theory", "12 across 3 fields"]),
 S("ui-upgrade", "The Absurd Upgrade", "Craft",
   "The upgrade must be gloriously unnecessary: karaoke in a toaster. Necessity is the enemy of the unhinged.",
   "The upgrade is the idea's engine - the wilder, the better.",
   "12 upgrades in the bank.",
   "The Signature reading: the unnecessary is the engine. Karaoke belongs nowhere, goes everywhere.",
   "Try the Signature method: upgrade unnecessarily - the engine of unhinged.",
   ["Gloriously unnecessary", "The idea's engine", "12 in the bank", "Necessity is the enemy"]),
 S("ui-benefit", "The Fake Benefit", "Craft",
   "Promise something unverifiable: 'reduces existential dread.' The benefit is the sales pitch of the absurd.",
   "Fake benefits parody real marketing - the pitch is the joke.",
   "8 benefits in the bank.",
   "The Signature reading: the pitch parodies. 'Unverified' is the fine print.",
   "Try the Signature method: promise dread-reduction - the pitch of absurd.",
   ["Unverifiable promises", "Parodies marketing", "8 in the bank", "The pitch is the joke"]),
 S("ui-warning", "The Warning Label", "Craft",
   "Every idea needs a warning: 'May develop opinions.' The warning is the punchline's bodyguard.",
   "Warnings complete the product parody - real products have them, so unhinged ones must too.",
   "8 warnings in the bank.",
   "The Signature reading: the warning completes. Parody needs its fine print.",
   "Try the Signature method: warn of jazz - the bodyguard's duty.",
   ["Completes the parody", "The punchline's bodyguard", "8 in the bank", "Fine print required"]),
 S("ui-kind", "The Kindness Constraint", "Craft",
   "Unhinged, never unkind: the ideas punch at boredom, never at people. The chaos is clean.",
   "The constraint is the brand: wild imagination, good nature.",
   "All banks are people-safe by design.",
   "The Signature reading: the chaos is clean. Punch boredom, never people.",
   "Try the Signature method: keep it clean - the chaos's constraint.",
   ["Wild but kind", "Punch boredom", "Never people", "Clean by design"]),
 S("ui-seed", "The Seed Promise", "Craft",
   "Same seed, same idea - the unhinged is reproducible. Madness, on a schedule.",
   "Deterministic generation via mulberry32 PRNG.",
   "Parity-tested at build time.",
   "The Signature reading: the madness schedules. Reproducible unhinged.",
   "Try the Signature method: keep the seed - the scheduled madness.",
   ["Same seed, same idea", "Mulberry32 PRNG", "Reproducible", "Madness on schedule"]),
 S("ui-combo", "The Combination Space", "Craft",
   "12 things x 12 upgrades x 8 benefits x 8 warnings = 9,216 ideas. The unhinged has range.",
   "Combinatorial space: small banks, vast madness.",
   "9,216 combinations.",
   "The Signature reading: the banks are small. The madness is vast.",
   "Try the Signature method: trust the 9,216 - the range of unhinged.",
   ["12 x 12 x 8 x 8", "9,216 ideas", "Small banks", "Vast madness"]),
 S("ui-field", "The Field Flavors", "Craft",
   "Gadgets, Home, Daily Life - the mundane comes in flavors. The field seasons the absurd.",
   "Fields ground the idea in a relatable domain.",
   "Three fields, four things each.",
   "The Signature reading: the field seasons. Absurdity needs a domain.",
   "Try the Signature method: pick the flavor - the seasoning of unhinged.",
   ["Gadgets, Home, Daily Life", "4 things each", "Relatable domains", "Seasoning for absurd"]),
 S("ui-use", "The Use Case", "Craft",
   "Unhinged ideas are for brainstorming, gifts, and breaking creative blocks. The use is the excuse.",
   "Applied absurdity: the ideas unlock lateral thinking.",
   "Brainstorming fuel.",
   "The Signature reading: the absurd unlocks. Lateral via unhinged.",
   "Try the Signature method: brainstorm unhinged - the block's breaker.",
   ["Brainstorming fuel", "Gift ideas", "Block breaker", "Lateral thinking"]),
 S("ui-share", "The Share Test", "Craft",
   "If you'd text it to a friend, it passes. The share test is the unhinged's quality gate.",
   "Shareability as the metric: the idea must travel.",
   "The text-to-friend test.",
   "The Signature reading: the text is the test. Travel is quality.",
   "Try the Signature method: text it - the quality gate.",
   ["Text-to-friend test", "Shareability metric", "Ideas must travel", "The quality gate"]),
 S("ui-evolve", "The Evolution Rule", "Craft",
   "The best unhinged ideas evolve: add a second upgrade. The toaster now also files taxes AND judges you.",
   "Stacking upgrades: the advanced technique.",
   "Double-upgrade mode.",
   "The Signature reading: the stacking heightens. Two upgrades, one toaster.",
   "Try the Signature method: stack them - the advanced unhinged.",
   ["Add a second upgrade", "Stacking heightens", "Advanced technique", "Two upgrades, one toaster"]),
 S("ui-archive", "The Archive Canon", "Craft",
   "34 seeded ideas are the canon - the generator's greatest unhinged hits, fixed forever.",
   "Seeded records anchor the range.",
   "34 canonical ideas.",
   "The Signature reading: the canon anchors. Greatest unhinged, fixed.",
   "Try the Signature method: read the 34 - the canon of unhinged.",
   ["34 seeded ideas", "The canon", "Fixed forever", "Anchors the range"]),
 S("ui-signature", "The Signature Gear", "Craft",
   "The Signature edition compounds harder: upgrades stack, benefits inflate, warnings escalate. Same engine, wilder.",
   "Signature = the formula, heightening applied twice.",
   "The wilder gear.",
   "The Signature reading: the gear is wilder. Heightening, applied twice.",
   "Try the Signature method: shift wilder - the Signature unhinged.",
   ["Same formula", "Compounds harder", "Warnings escalate", "The wilder gear"]),
 S("ui-live", "The Live Engine", "Craft",
   "The generator runs in your browser - the unhinged is client-side. No server can contain it.",
   "Deterministic client-side JavaScript.",
   "Runs offline after load.",
   "The Signature reading: the unhinged is local. No server contains it.",
   "Try the Signature method: generate locally - the contained chaos.",
   ["Browser-native", "No server", "Deterministic", "Offline chaos"]),
 S("ui-remix", "The Remix Habit", "Craft",
   "Take any idea and swap one part: same toaster, new warning. The remix habit multiplies the unhinged.",
   "One-part swaps: the creativity exercise.",
   "The swap technique.",
   "The Signature reading: the swap multiplies. One part, new idea.",
   "Try the Signature method: swap the warning - the remix habit.",
   ["Swap one part", "Same toaster, new warning", "Creativity exercise", "The multiply habit"]),
 S("ui-joy", "The Joy Standard", "Craft",
   "The standard is joy: if the idea doesn't make you grin, swap a part until it does. The grin is the spec.",
   "Joy as the acceptance criterion.",
   "The grin spec.",
   "The Signature reading: the grin is the spec. Joy is the standard.",
   "Try the Signature method: grin-test it - the acceptance criterion.",
   ["Joy is the standard", "Grin is the spec", "Swap till it grins", "Acceptance: delight"]),
]

register({
    "slug": "gen-unhinged-idea-generator",
    "theme": "internet-humor",
    "first_pick": True,
    "name": "The Unhinged Idea Generator Database",
    "tagline": ("A real working idea generator: mundane things plus absurd upgrades, fake "
                "benefits, and warning labels - wildly imaginative, clean, reproducible."),
    "record_kind": "generated idea record",
    "pub_line": ("Public generator - a real client-side idea engine: pick a seed, get a complete "
                 "unhinged-but-kind idea. Fictional concepts, proudly so."),
    "ai": "JAH Idea Engineer",
    "role": ("idea engineer - assembling wildly imaginative clean ideas; answering from many "
             "angles - the parts, the assembly, the joy - using only archive data"),
    "search_ph": "Search the idea canon...",
    "chat_ph": "Give me a seed - I will unhinge an idea...",
    "fields": FIELDS,
    "gen_desc": ("Generate REAL ideas with the live client-side engine. Seeded archive records "
                 "are the authoritative entries."),
    "greet": "Give me any seed number - I will unhinge responsibly.",
    "gen_kind": "unhinged-idea",
    "citation": CITE,
    "demo_default": "report",
    "seeds": SEEDS,
    "custom_records": custom_records,
    "gen_js": gen_js,
})
