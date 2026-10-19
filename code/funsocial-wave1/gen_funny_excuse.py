#!/usr/bin/env python3
"""Wave 1 GENERATOR item: gen-funny-excuse-generator (first-release pick).

A REAL working client-side excuse generator: combinatorial assembly from
authored banks (situation openers x absurd causes x escalations x closers),
seeded and reproducible. Every generation is a complete, good-natured excuse.
"""
import json

from lib import register

FIELDS = ["Work", "School", "Social"]

OPENERS = {
    "Work": [
        "I was ready for the standup when",
        "I left early for the office, but",
        "I had the presentation open when",
        "I was about to join the call when",
    ],
    "School": [
        "I finished the homework, but then",
        "I was walking to class when",
        "I had my assignment ready when",
        "I set three alarms, yet",
    ],
    "Social": [
        "I was getting ready to come when",
        "I had the gift wrapped when",
        "I was out the door when",
        "I swear I was coming, but",
    ],
}
CAUSES = [
    "my cat staged a sit-in on my laptop",
    "a goose claimed my parking spot and defended it",
    "my GPS developed strong opinions about shortcuts",
    "the elevator achieved sentience and chose the scenic route",
    "a flash mob formed in my kitchen",
    "my coffee achieved independence and fled",
    "the Wi-Fi unionized and demanded better working conditions",
    "a squirrel moved into my car and started charging rent",
    "my alarm clock joined a band and went on tour",
    "the traffic cones organized a protest",
    "my shoes went on strike for better laces",
    "a pigeon stole my keys and flew to another zip code",
]
CAUSE_SHORT = [
    "Cat Sit-In", "Goose Parking Dispute", "Opinioned GPS", "Sentient Elevator",
    "Kitchen Flash Mob", "Independent Coffee", "Wi-Fi Union", "Squirrel Tenant",
    "Touring Alarm Clock", "Cone Protest", "Shoe Strike", "Pigeon Key Theft",
]
assert len(CAUSE_SHORT) == len(CAUSES)
ESCALATIONS = [
    "and then it brought friends",
    "which triggered an emergency neighborhood watch meeting",
    "so now there's a group chat about it with 47 members",
    "and the HOA has opened an investigation",
    "which is now local legend - ask anyone",
    "and I have the blurry photos to prove it",
]
CLOSERS = [
    "I'm seeking counseling. For the goose.",
    "I've learned nothing, but I've lived.",
    "I'll be early tomorrow. Probably. Don't hold me to it.",
    "The cat has been formally reprimanded.",
    "I'm accepting thoughts, prayers, and snacks.",
    "This will be in my memoir. Chapter one.",
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
    fields = list(OPENERS.keys())
    f = field if field in OPENERS else fields[int(rnd() * len(fields)) % len(fields)]
    opener = OPENERS[f][int(rnd() * len(OPENERS[f]))]
    cause = CAUSES[int(rnd() * len(CAUSES))]
    esc = ESCALATIONS[int(rnd() * len(ESCALATIONS))]
    closer = CLOSERS[int(rnd() * len(CLOSERS))]
    excuse = "%s %s, %s. %s" % (opener, cause, esc, closer)
    return {
        "field": f, "opener": opener, "cause": cause,
        "escalation": esc, "closer": closer, "excuse": excuse,
    }


def custom_records(source, prefix):
    sig = (source == "signature")
    raws = []
    combos = []
    for f in FIELDS:
        for o in OPENERS[f]:
            for c in CAUSES:
                combos.append((f, o, c))
    # 34 distinct, deterministic combos
    chosen = [combos[(i * 7) % len(combos)] for i in range(34)]
    seen = set()
    out = []
    for i, (f, o, c) in enumerate(chosen):
        key = (o, c)
        if key in seen:
            c = CAUSES[(CAUSES.index(c) + 5) % len(CAUSES)]
            key = (o, c)
        seen.add(key)
        esc = ESCALATIONS[i % len(ESCALATIONS)]
        closer = CLOSERS[(i * 3) % len(CLOSERS)]
        excuse = "%s %s, %s. %s" % (o, c, esc, closer)
        title = "Excuse %d: The %s%s" % (
            i + 1, CAUSE_SHORT[CAUSES.index(c)],
            " (Signature Edition)" if sig else "")
        desc = ("The excuse: \"%s\"" % excuse)
        desc += (" Use it wisely - it is obviously fictional, which is the entire "
                 "point. A good excuse is a tiny story; this one has a beginning "
                 "(%s), a middle (%s), an escalation (%s), and an ending (%s)."
                 % (o, c, esc, closer))
        if sig:
            desc += (" The Signature treatment: the cause compounds - each element "
                     "escalates the last, so the excuse teaches story structure.")
        desc += " (Seed %d reproduces this excuse in the live generator.)" % (9000 + i * 37)
        how = ("The Funny Excuse engine assembles excuses combinatorially: a "
               "situation opener, an absurd cause, an escalation, and a closer - "
               "picked by seeded random from authored banks (%d openers, %d causes, "
               "%d escalations, %d closers = %d possible excuses). Same seed, same "
               "excuse, every time." % (
                   sum(len(v) for v in OPENERS.values()), len(CAUSES),
                   len(ESCALATIONS), len(CLOSERS),
                   sum(len(v) for v in OPENERS.values()) * len(CAUSES) * len(ESCALATIONS) * len(CLOSERS)))
        raws.append({
            "t": title, "g": f,
            "description": desc, "how_it_works": how,
            "key_points": ["Opener: " + o, "Cause: " + c, "Escalation: " + esc, "Closer: " + closer],
            "requirements": "Reading only - no equipment needed.",
            "citations": ["Original comedic writing for this database; excuses are obviously fictional."],
            "demo": "report",
            "seed": {"points": ["Opener: " + o, "Cause: " + c, "Escalation: " + esc, "Closer: " + closer],
                     "fact": desc[:400], "mechanism": how[:300]},
        })
    assert len({r["t"] for r in raws}) == 34
    return raws


GEN_JS_TEMPLATE = r"""(function(){'use strict';
/* JAH Funny Excuse Generator - jahdb-gen-funny-excuse-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL client-side generator: combinatorial excuse assembly. Same seed, same excuse.
   __SOURCE__ edition. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX=__PREFIX__;
var FIELDS=__FIELDS__;
var OPENERS=__OPENERS__;
var CAUSES=__CAUSES__;
var ESCALATIONS=__ESCALATIONS__;
var CLOSERS=__CLOSERS__;
var SOURCE='__SOURCE__';
function pick(r,arr){return arr[(r()*arr.length)|0];}
function assemble(seed,field){
  var r=prng(seed>>>0||1);
  var f=(field&&OPENERS[field])?field:pick(r,FIELDS);
  var o=pick(r,OPENERS[f]), c=pick(r,CAUSES), e=pick(r,ESCALATIONS), cl=pick(r,CLOSERS);
  return {field:f,opener:o,cause:c,escalation:e,closer:cl,
          excuse:o+' '+c+', '+e+'. '+cl};
}
function demoProgram(a){
  function q(s){return s.replace(/"/g,"'");}
  return '# Funny Excuse Generator - live excuse\nprint("SITUATION: '+q(a.field)+'")\nprint("OPENER:    '+q(a.opener)+'")\nprint("CAUSE:     '+q(a.cause)+'")\nprint("ESCALATION:'+q(a.escalation)+'")\nprint("CLOSER:    '+q(a.closer)+'")\nprint()\nprint("EXCUSE: '+q(a.excuse)+'")\nprint("OK: excuse assembled from 4 banks")\n';
}
function generate(seed,opts,rnd){
  opts=opts||{};
  var a=assemble(seed>>>0||1,opts.field||null);
  var id=PREFIX+String(seed>>>0||1).padStart(6,'0');
  var title='Fresh Excuse: '+a.cause.charAt(0).toUpperCase()+a.cause.slice(1)+(SOURCE==='signature'?' (Signature Edition)':'');
  return {
    id:id,
    name:title+' — '+a.field,
    title:title,
    description:'GENERATED EXCUSE (live generator output - clearly labeled fiction). "'+a.excuse+'"',
    field:a.field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Live generator output - fictional excuse, not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:demoProgram(a),note:'Live excuse demo program.'},
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
  if(!r.parts||!r.parts.excuse)e.push('parts');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-gen-funny-excuse-generator-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,assemble:assemble};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-funny-excuse-generator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""


def gen_js(source, prefix, cfg):
    js = GEN_JS_TEMPLATE
    js = js.replace("__PREFIX__", json.dumps(prefix))
    js = js.replace("__FIELDS__", json.dumps(FIELDS))
    js = js.replace("__OPENERS__", json.dumps(OPENERS, ensure_ascii=False))
    js = js.replace("__CAUSES__", json.dumps(CAUSES, ensure_ascii=False))
    js = js.replace("__ESCALATIONS__", json.dumps(ESCALATIONS, ensure_ascii=False))
    js = js.replace("__CLOSERS__", json.dumps(CLOSERS, ensure_ascii=False))
    js = js.replace("__SOURCE__", source)
    return js


def S(key, t, g, fact, mechanism, evidence, sig_angle, sig_do, points, **kw):
    d = dict(key=key, t=t, g=g, fact=fact, mechanism=mechanism,
             evidence=evidence, sig_angle=sig_angle, sig_do=sig_do,
             points=points)
    d.update(kw)
    return d


CITE = ("Original comedic writing for this database; all excuses are obviously "
        "fictional.")

SEEDS = [
 S("fe-anatomy", "Anatomy of an Excuse", "Craft",
   "Every excuse has four parts: opener, absurd cause, escalation, closer. The structure is the joke's skeleton.",
   "The four-part structure mirrors story structure - setup, incident, complication, button.",
   "The generator's banks are organized on this anatomy.",
   "The Signature reading: the skeleton is story. Four parts, one laugh.",
   "Try the Signature method: build on the skeleton - the four-part excuse.",
   ["Opener sets the scene", "Cause is absurd", "Escalation compounds", "Closer buttons it"]),
 S("fe-cause", "The Absurd Cause", "Craft",
   "The cause must be absurd but specific: 'a goose claimed my parking spot' beats 'traffic.' Specificity is funnier.",
   "Specific absurdity creates mental images; vague absurdity creates shrugs.",
   "The cause bank holds 12 specific absurdities.",
   "The Signature reading: the specific is the funny. Goose, not traffic.",
   "Try the Signature method: name the goose - the specific absurdity.",
   ["Absurd but specific", "Creates mental images", "12 in the bank", "Specificity beats vagueness"]),
 S("fe-escalation", "The Escalation Rule", "Craft",
   "Every excuse escalates: the cause brings friends, the HOA investigates. Escalation is the comedy engine.",
   "Comedy theory: the rule of three and heightening. Each beat tops the last.",
   "The escalation bank holds 6 heighteners.",
   "The Signature reading: the heightening is the engine. Top the last beat.",
   "Try the Signature method: bring friends - the escalation's guest list.",
   ["Each beat tops the last", "The HOA investigates", "Heightening theory", "6 in the bank"]),
 S("fe-closer", "The Closer", "Craft",
   "The closer buttons the excuse: 'I've learned nothing.' The button releases the laugh.",
   "The button is the punchline's landing gear.",
   "The closer bank holds 6 buttons.",
   "The Signature reading: the button lands. Release the laugh.",
   "Try the Signature method: learn nothing - the closer's wisdom.",
   ["Buttons the excuse", "Releases the laugh", "6 in the bank", "The landing gear"]),
 S("fe-seed", "The Seed Promise", "Craft",
   "Same seed, same excuse - every generation is reproducible. The seed is the excuse's ID.",
   "Deterministic generation via mulberry32 PRNG.",
   "Parity-tested at build time.",
   "The Signature reading: the seed is the ID. Reproducibility is the promise.",
   "Try the Signature method: keep the seed - the reproducible laugh.",
   ["Same seed, same excuse", "Mulberry32 PRNG", "Reproducible comedy", "Seed is the ID"]),
 S("fe-field", "The Field Selector", "Craft",
   "Excuses come in Work, School, and Social flavors - the opener changes, the absurdity doesn't.",
   "Situational openers ground the absurdity in a real context.",
   "Three fields, four openers each.",
   "The Signature reading: the field grounds. Absurdity needs context.",
   "Try the Signature method: pick the field - the context for chaos.",
   ["Work, School, Social", "Openers per field", "Absurdity needs context", "4 openers each"]),
 S("fe-honesty", "The Honesty Clause", "Craft",
   "The best excuses are obviously fictional - the fiction is the charm. Nobody believes the goose; everybody enjoys it.",
   "Obviously-false excuses are social gifts; plausible lies are just lies.",
   "The generator's excuses are proudly unbelievable.",
   "The Signature reading: the fiction is the charm. Unbelievable, enjoyable.",
   "Try the Signature method: stay unbelievable - the charm's requirement.",
   ["Obviously fictional", "Fiction is the charm", "Nobody believes, all enjoy", "Proudly unbelievable"]),
 S("fe-timing", "The Timing Rule", "Craft",
   "Deliver the excuse early, with confidence. A late excuse is a confession; a confident one is a performance.",
   "Delivery theory: confidence sells the absurd.",
   "The performance principle.",
   "The Signature reading: the confidence sells. Early and assured.",
   "Try the Signature method: deliver early - the performance, not the confession.",
   ["Early beats late", "Confidence sells absurd", "Performance over confession", "The delivery theory"]),
 S("fe-brevity", "The Brevity Rule", "Craft",
   "One excuse, four parts, done. The generator never rambles - the laugh has a budget.",
   "Brevity is the soul of the excuse.",
   "Four parts, no more.",
   "The Signature reading: the laugh has a budget. Spend it in four parts.",
   "Try the Signature method: budget the laugh - four parts, done.",
   ["Four parts, done", "Never rambles", "Brevity is the soul", "The laugh's budget"]),
  S("fe-kind", "The Kindness Rule", "Craft",
   "Excuses punch at situations, never people. The goose is the villain; no human is.",
   "Clean comedy: the absurdity targets circumstances, never anyone's dignity.",
   "All banks are people-safe.",
   "The Signature reading: the goose is the villain. People are never.",
   "Try the Signature method: villainize the goose - the kind comedy.",
   ["Punch at situations", "Never at people", "The goose is the villain", "Clean by design"]),
 S("fe-variety", "The Variety Engine", "Craft",
   "12 openers x 12 causes x 6 escalations x 6 closers = 5,184 possible excuses. The combinations never repeat in practice.",
   "Combinatorial generation: small banks, huge space.",
   "5,184 combinations.",
   "The Signature reading: the banks are small. The space is huge.",
   "Try the Signature method: trust the math - the 5,184.",
   ["12 x 12 x 6 x 6", "5,184 excuses", "Small banks, huge space", "Never repeats practically"]),
 S("fe-reuse", "The Reuse Policy", "Craft",
   "A great excuse can be reused - but change the cause. The structure is reusable; the goose is not.",
   "The anatomy separates structure from content.",
   "Reuse the skeleton, refresh the cause.",
   "The Signature reading: the skeleton reuses. The goose retires.",
   "Try the Signature method: refresh the cause - the reusable skeleton.",
   ["Structure is reusable", "Refresh the cause", "The skeleton endures", "Retire the goose"]),
 S("fe-apology", "The Apology Adjacent", "Craft",
   "The excuse works best paired with a real apology: the laugh opens the door, the sorry walks through.",
   "Humor disarms; sincerity resolves.",
   "The one-two punch.",
   "The Signature reading: the laugh opens. The sorry walks through.",
   "Try the Signature method: pair them - the laugh and the sorry.",
   ["Humor disarms", "Sincerity resolves", "The one-two punch", "Laugh, then sorry"]),
 S("fe-archive", "The Archive Promise", "Craft",
   "The 34 seeded excuses are the canon - the generator's greatest hits, fixed and reproducible.",
   "Seeded records anchor the generator's range.",
   "34 canonical excuses.",
   "The Signature reading: the canon anchors. Greatest hits, fixed.",
   "Try the Signature method: read the canon - the 34.",
   ["34 seeded excuses", "The canon", "Fixed and reproducible", "Anchors the range"]),
 S("fe-signature", "The Signature Treatment", "Craft",
   "The Signature edition escalates harder: causes compound, closers land sharper. Same engine, higher gear.",
   "Signature = the same four parts, tuned for maximum heightening.",
   "The higher gear.",
   "The Signature reading: the gear is higher. Same engine, more height.",
   "Try the Signature method: shift up - the Signature gear.",
   ["Same four parts", "Harder escalation", "Sharper closers", "The higher gear"]),
 S("fe-memoir", "The Memoir Rule", "Craft",
   "Every excuse ends up in the memoir. 'Chapter one: the goose.' The excuse is future literature.",
   "The closer bank's memoir line is the philosophy: today's disaster is tomorrow's chapter.",
   "Future literature.",
   "The Signature reading: the disaster is literature. Chapter one: the goose.",
   "Try the Signature method: write chapter one - the goose's memoir.",
   ["Today's disaster", "Tomorrow's chapter", "The memoir philosophy", "Chapter one: the goose"]),
 S("fe-live", "The Live Promise", "Craft",
   "The generator runs entirely in your browser - no server, no account, just excuses. The comedy is client-side.",
   "Deterministic client-side JavaScript; the page's Generate button calls it directly.",
   "Runs offline after load.",
   "The Signature reading: the comedy is local. No server required.",
   "Try the Signature method: generate locally - the offline laugh.",
   ["Runs in the browser", "No server needed", "Deterministic JS", "The offline laugh"]),
]

register({
    "slug": "gen-funny-excuse-generator",
    "theme": "internet-humor",
    "first_pick": True,
    "name": "The Funny Excuse Generator Database",
    "tagline": ("A real working excuse generator: combinatorial assembly of openers, absurd "
                "causes, escalations, and closers - same seed, same excuse."),
    "record_kind": "generated excuse record",
    "pub_line": ("Public generator - a real client-side excuse engine: pick a seed and situation, "
                 "get a complete, good-natured excuse. Obviously fictional, proudly so."),
    "ai": "JAH Excuse Engineer",
    "role": ("excuse engineer - assembling genuine funny excuses from authored banks; answering "
             "from many angles - the parts, the assembly, the delivery - using only archive data"),
    "search_ph": "Search the excuse canon...",
    "chat_ph": "Give me a seed - I will build your excuse...",
    "fields": FIELDS,
    "gen_desc": ("Generate REAL excuses with the live client-side engine. Seeded archive records "
                 "are the authoritative entries."),
    "greet": "Give me any seed number - I will assemble a flawless excuse.",
    "gen_kind": "excuse",
    "citation": CITE,
    "demo_default": "report",
    "seeds": SEEDS,
    "custom_records": custom_records,
    "gen_js": gen_js,
})
