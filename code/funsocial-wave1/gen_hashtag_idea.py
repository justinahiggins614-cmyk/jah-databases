#!/usr/bin/env python3
"""Wave 1 GENERATOR item: gen-hashtag-idea-generator (first-release pick).

A REAL working client-side hashtag generator: topic banks x 8 style transforms
(alliteration, pun, portmanteau, rhyme, contrast, exaggeration, relatable,
aspirational) x twist suffixes, with length validation, retry logic, and a
computed shareability score. Seeded and reproducible.
"""
import json

from lib import register

FIELDS = ["Food & Drink", "Days", "Animals", "Lifestyle"]

TOPICS = {
    "Food & Drink": ["coffee", "pizza"],
    "Days": ["monday", "friday", "weekend"],
    "Animals": ["cat", "dog"],
    "Lifestyle": ["gym", "book", "nap", "wifi", "plant"],
}

ADJECTIVES = {
    "c": ["Cozy", "Chaotic", "Caffeinated"],
    "p": ["Peaceful", "Playful", "Powerful"],
    "m": ["Moody", "Motivated", "Messy"],
    "f": ["Fresh", "Fearless", "Funny"],
    "w": ["Wild", "Warm", "Wacky"],
    "g": ["Glorious", "Goofy", "Gritty"],
    "b": ["Bold", "Breezy", "Bright"],
    "d": ["Daring", "Dreamy", "Delightful"],
    "n": ["Nifty", "Noble", "Neat"],
}
PUNS = {
    "coffee": ["BrewHaha", "EspressoYourself"],
    "pizza": ["SliceToMeetYou", "SliceSliceBaby"],
    "monday": ["Mondaze", "MonYay"],
    "friday": ["FriYay", "FridayFeeling"],
    "weekend": ["WeekendWarrior", "SleepEnd"],
    "cat": ["Purrfection", "MeowMania"],
    "dog": ["PawSome", "PupCulture"],
    "gym": ["FlexFest", "SwolePatrol"],
    "book": ["ShelfAware", "NovelIdea"],
    "nap": ["NapQueen", "SleepOnIt"],
    "wifi": ["StreamDream", "ConnectedChaos"],
    "plant": ["SproutAbout", "LeafItToMe"],
}
RHYMES = {
    "coffee": ["CoffeeToffee", "LattePatter"],
    "pizza": ["CheesyBreezy", "PizzaFesta"],
    "monday": ["MondayFunday", "MondayRunDay"],
    "friday": ["FridayMyDay", "FridaySkyHigh"],
    "weekend": ["WeekendBlend", "WeekendUnwind"],
    "cat": ["CatChat", "CatHat"],
    "dog": ["DogBlog", "DogJog"],
    "gym": ["TrainGain", "PumpJump"],
    "book": ["BookNook", "ReadFeed"],
    "nap": ["NapTrap", "NapClap"],
    "wifi": ["WifiHiFi", "WifiSciFi"],
    "plant": ["PlantChant", "LeafRelief"],
}
PORTMANTEAU_TAILS = ["aholic", "ista", "ology", "verse"]
TWISTS = ["", "Life", "Club", "Era", "Mode", "Daily", "Chronicles"]
STYLES = ["alliteration", "pun", "portmanteau", "rhyme",
          "contrast", "exaggeration", "relatable", "aspirational"]


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


def _pick(rnd, arr):
    return arr[int(rnd() * len(arr))]


def build_tag(topic, style, rnd, twist):
    cap = topic.capitalize()
    if style == "alliteration":
        adj = _pick(rnd, ADJECTIVES[topic[0]])
        core, label = adj + cap, "alliteration: %s + %s" % (adj, cap)
    elif style == "pun":
        core, label = _pick(rnd, PUNS[topic]), "pun on '%s'" % topic
    elif style == "portmanteau":
        tail = _pick(rnd, PORTMANTEAU_TAILS)
        core, label = cap + tail, "portmanteau: %s + %s" % (cap, tail)
    elif style == "rhyme":
        core, label = _pick(rnd, RHYMES[topic]), "rhyme on '%s'" % topic
    elif style == "contrast":
        core, label = cap + "VsReality", "contrast: %s vs reality" % cap
    elif style == "exaggeration":
        pre = _pick(rnd, ["Ultra", "Extreme", "Mega"])
        core, label = pre + cap, "exaggeration: %s %s" % (pre, cap)
    elif style == "relatable":
        core, label = "Relatable" + cap, "relatable: shared %s experience" % topic
    else:
        core, label = cap + "Goals", "aspirational: %s goals" % cap
    return "#" + core + twist, label


def score_tag(tag, style):
    s = 100 - 2 * max(0, len(tag) - 16)
    if style == "alliteration":
        s += 10
    if len(tag) <= 14:
        s += 5
    return max(0, min(100, s))


def assemble(seed, field=None):
    rnd = make_prng(seed)
    fields = list(TOPICS.keys())
    f = field if field in TOPICS else _pick(rnd, fields)
    topic = _pick(rnd, TOPICS[f])
    style = _pick(rnd, STYLES)
    # length validation with retry: drop the twist, then shorten style choices
    tag, label, twist, tries = "", "", "", 0
    while tries < 4:
        twist = _pick(rnd, TWISTS) if tries < 2 else ""
        tag, label = build_tag(topic, style, rnd, twist)
        if len(tag) <= 24:
            break
        tries += 1
    sc = score_tag(tag, style)
    return {"field": f, "topic": topic, "style": style, "twist": twist or "(none)",
            "hashtag": tag, "technique": label, "score": sc,
            "length": len(tag)}


def custom_records(source, prefix):
    sig = (source == "signature")
    topics_all = [t for ts in TOPICS.values() for t in ts]
    raws = []
    for i in range(34):
        topic = topics_all[i % len(topics_all)]
        style = STYLES[(i // len(topics_all)) % len(STYLES)]
        rnd = make_prng(3000 + i * 91)
        twist = TWISTS[i % len(TWISTS)]
        tag, label = build_tag(topic, style, rnd, twist)
        if len(tag) > 24:
            tag, label = build_tag(topic, style, rnd, "")
            twist = "(none)"
        sc = score_tag(tag, style)
        f = next(ff for ff, ts in TOPICS.items() if topic in ts)
        title = "Hashtag %d: %s%s" % (i + 1, tag, " (Signature Edition)" if sig else "")
        desc = ("The hashtag: %s  Technique: %s. " % (tag, label))
        desc += ("Built from topic '%s' in %s, styled as %s%s, scoring %d/100 on the "
                 "shareability scale (length %d chars%s). " % (
                     topic, f, style, " with twist '%s'" % twist if twist not in ("", "(none)") else "",
                     sc, len(tag),
                     " - alliteration bonus applied" if style == "alliteration" else ""))
        desc += ("A good hashtag is short, evocative, and typed without thinking; "
                 "this one was engineered for exactly that.")
        if sig:
            desc += (" The Signature treatment: style and twist are chosen to compound "
                     "- the technique reinforces the topic's energy.")
        desc += " (Seed %d reproduces this hashtag in the live generator.)" % (3000 + i * 91)
        how = ("The Hashtag engine picks a topic from %d across %s, applies one of 8 "
               "style transforms (alliteration, pun, portmanteau, rhyme, contrast, "
               "exaggeration, relatable, aspirational), appends a twist suffix, then "
               "validates length (<=24 chars, retrying without the twist) and scores "
               "shareability from length and technique. Seeded and reproducible."
               % (len(topics_all), ", ".join(FIELDS)))
        raws.append({
            "t": title, "g": f,
            "description": desc, "how_it_works": how,
            "key_points": ["Hashtag: " + tag, "Topic: " + topic, "Style: " + style,
                           "Shareability score: %d/100" % sc],
            "requirements": "Reading only - no equipment needed.",
            "citations": ["Original hashtag craft for this database."],
            "demo": "report",
            "seed": {"points": ["Hashtag: " + tag, "Topic: " + topic, "Style: " + style,
                                "Shareability score: %d/100" % sc],
                     "fact": desc[:400], "mechanism": how[:300]},
        })
    assert len({r["t"] for r in raws}) == 34
    return raws


GEN_JS_TEMPLATE = r"""(function(){'use strict';
/* JAH Hashtag Idea Generator - jahdb-gen-hashtag-idea-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL client-side generator: style transforms + validation + scoring. Same seed, same hashtag.
   __SOURCE__ edition. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX=__PREFIX__;
var FIELDS=__FIELDS__;
var TOPICS=__TOPICS__;
var ADJECTIVES=__ADJECTIVES__;
var PUNS=__PUNS__;
var RHYMES=__RHYMES__;
var TAILS=__TAILS__;
var TWISTS=__TWISTS__;
var STYLES=__STYLES__;
var SOURCE='__SOURCE__';
function pick(r,arr){return arr[(r()*arr.length)|0];}
function cap(s){return s.charAt(0).toUpperCase()+s.slice(1);}
function buildTag(topic,style,r,twist){
  var c=cap(topic), core, label;
  if(style==='alliteration'){var adj=pick(r,ADJECTIVES[topic.charAt(0)]);core=adj+c;label='alliteration: '+adj+' + '+c;}
  else if(style==='pun'){core=pick(r,PUNS[topic]);label="pun on '"+topic+"'";}
  else if(style==='portmanteau'){var tail=pick(r,TAILS);core=c+tail;label='portmanteau: '+c+' + '+tail;}
  else if(style==='rhyme'){core=pick(r,RHYMES[topic]);label="rhyme on '"+topic+"'";}
  else if(style==='contrast'){core=c+'VsReality';label='contrast: '+c+' vs reality';}
  else if(style==='exaggeration'){var pre=pick(r,['Ultra','Extreme','Mega']);core=pre+c;label='exaggeration: '+pre+' '+c;}
  else if(style==='relatable'){core='Relatable'+c;label='relatable: shared '+topic+' experience';}
  else {core=c+'Goals';label='aspirational: '+c+' goals';}
  return {tag:'#'+core+twist,label:label};
}
function scoreTag(tag,style){
  var s=100-2*Math.max(0,tag.length-16);
  if(style==='alliteration')s+=10;
  if(tag.length<=14)s+=5;
  return Math.max(0,Math.min(100,s));
}
function assemble(seed,field){
  var r=prng(seed>>>0||1);
  var f=(field&&TOPICS[field])?field:pick(r,FIELDS);
  var topic=pick(r,TOPICS[f]), style=pick(r,STYLES);
  var tag='',label='',twist='',tries=0;
  while(tries<4){
    twist=tries<2?pick(r,TWISTS):'';
    var b=buildTag(topic,style,r,twist);tag=b.tag;label=b.label;
    if(tag.length<=24)break;
    tries++;
  }
  return {field:f,topic:topic,style:style,twist:twist||'(none)',hashtag:tag,
          technique:label,score:scoreTag(tag,style),length:tag.length};
}
function demoProgram(a){
  function q(s){return String(s).replace(/"/g,"'");}
  return '# Hashtag Idea Generator - live hashtag\nprint("FIELD:    '+q(a.field)+'")\nprint("TOPIC:    '+q(a.topic)+'")\nprint("STYLE:    '+q(a.style)+'")\nprint("TWIST:    '+q(a.twist)+'")\nprint("TECHNIQUE:'+q(a.technique)+'")\nprint()\nprint("HASHTAG: '+q(a.hashtag)+'")\nprint("SCORE: %d/100, LENGTH: %d chars" % ('+a.score+', '+a.length+'))\nprint("OK: hashtag built, validated, and scored")\n';
}
function generate(seed,opts,rnd){
  opts=opts||{};
  var a=assemble(seed>>>0||1,opts.field||null);
  var id=PREFIX+String(seed>>>0||1).padStart(6,'0');
  var title='Fresh Hashtag: '+a.hashtag+(SOURCE==='signature'?' (Signature Edition)':'');
  return {
    id:id,
    name:title+' — '+a.field,
    title:title,
    description:'GENERATED HASHTAG (live generator output - clearly labeled). '+a.hashtag+' — '+a.technique+', shareability '+a.score+'/100.',
    field:a.field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Live generator output - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:demoProgram(a),note:'Live hashtag demo program.'},
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
  if(!r.parts||!r.parts.hashtag)e.push('parts');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-gen-hashtag-idea-generator-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,assemble:assemble,buildTag:buildTag,scoreTag:scoreTag};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-hashtag-idea-generator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""


def gen_js(source, prefix, cfg):
    js = GEN_JS_TEMPLATE
    js = js.replace("__PREFIX__", json.dumps(prefix))
    js = js.replace("__FIELDS__", json.dumps(FIELDS))
    js = js.replace("__TOPICS__", json.dumps(TOPICS, ensure_ascii=False))
    js = js.replace("__ADJECTIVES__", json.dumps(ADJECTIVES, ensure_ascii=False))
    js = js.replace("__PUNS__", json.dumps(PUNS, ensure_ascii=False))
    js = js.replace("__RHYMES__", json.dumps(RHYMES, ensure_ascii=False))
    js = js.replace("__TAILS__", json.dumps(PORTMANTEAU_TAILS))
    js = js.replace("__TWISTS__", json.dumps(TWISTS))
    js = js.replace("__STYLES__", json.dumps(STYLES))
    js = js.replace("__SOURCE__", source)
    return js


def S(key, t, g, fact, mechanism, evidence, sig_angle, sig_do, points, **kw):
    d = dict(key=key, t=t, g=g, fact=fact, mechanism=mechanism,
             evidence=evidence, sig_angle=sig_angle, sig_do=sig_do,
             points=points)
    d.update(kw)
    return d


CITE = "Original hashtag craft for this database."

SEEDS = [
 S("hh-anatomy", "Anatomy of a Hashtag", "Craft",
   "Every hashtag: topic + style transform + twist. The anatomy is small; the combinations are not.",
   "12 topics x 8 styles x 7 twists = 672 base combinations, before style sub-picks.",
   "The generator's banks implement the anatomy.",
   "The Signature reading: the anatomy is small. The combinations multiply.",
   "Try the Signature method: fill the three slots - the hashtag's anatomy.",
   ["Topic", "Style transform", "Twist suffix", "672 base combos"]),
 S("hh-topic", "The Topic Bank", "Craft",
   "12 topics across Food & Drink, Days, Animals, Lifestyle - the relatable nouns hashtags are built on.",
   "Topics are the hashtag's subject; familiarity is the fuel.",
   "12 topics, 4 fields.",
   "The Signature reading: the topic is familiar. Familiarity fuels.",
   "Try the Signature method: pick the relatable - the topic's fuel.",
   ["12 topics", "4 fields", "Relatable nouns", "Familiarity fuels"]),
 S("hh-styles", "The Eight Styles", "Craft",
   "Alliteration, pun, portmanteau, rhyme, contrast, exaggeration, relatable, aspirational - eight transforms, one topic.",
   "Style is the hashtag's voice; the transform chooses the register.",
   "8 style transforms.",
   "The Signature reading: the style is the voice. Eight registers.",
   "Try the Signature method: pick the register - the voice's transform.",
   ["8 transforms", "Style is voice", "Register per style", "One topic, eight voices"]),
  S("hh-allit", "The Alliteration Edge", "Craft",
   "Alliterative hashtags score +10: the ear remembers matching initials. #CozyCoffee beats #Coffee2.",
   "Phonesthetics: alliteration aids memory and typing.",
   "The scoring rewards it explicitly.",
   "The Signature reading: the ear remembers. Matching initials win.",
   "Try the Signature method: match the initial - the ear's reward.",
   ["+10 score bonus", "Aids memory", "The ear remembers", "Explicitly rewarded"]),
 S("hh-length", "The Length Law", "Craft",
   "Hashtags over 24 characters get rebuilt without the twist. Brevity is enforced, not suggested.",
   "Long hashtags don't get typed; the validation loop guarantees typability.",
   "Max 24 chars, retry logic.",
   "The Signature reading: the law enforces. Typability guaranteed.",
   "Try the Signature method: keep it typable - the law's demand.",
   ["Max 24 chars", "Retry without twist", "Brevity enforced", "Typability guaranteed"]),
 S("hh-score", "The Score", "Craft",
   "Every hashtag scores 0-100: length penalties, alliteration bonuses, short-tag rewards. The number is honest.",
   "Computed shareability: the score predicts typability and memorability.",
   "The formula is public.",
   "The Signature reading: the number is honest. Computed, not claimed.",
   "Try the Signature method: trust the formula - the honest number.",
   ["0-100 scale", "Length penalties", "Alliteration bonus", "Honest computation"]),
 S("hh-twist", "The Twist Suffix", "Craft",
   "Life, Club, Era, Mode, Daily, Chronicles - or nothing. The twist extends the hashtag's runway.",
   "Twists add community flavor: a Club is joinable, an Era is livable.",
   "7 twists including none.",
   "The Signature reading: the twist extends. Clubs are joinable.",
   "Try the Signature method: twist or not - the runway's choice.",
   ["7 options", "Community flavor", "Club is joinable", "Era is livable"]),
 S("hh-field", "The Field Map", "Craft",
   "Food & Drink, Days, Animals, Lifestyle - topics live in fields, and the generator can target any field.",
   "Fields let users generate on-theme: all pet hashtags, all Monday hashtags.",
   "4 fields, 12 topics.",
   "The Signature reading: the field targets. On-theme generation.",
   "Try the Signature method: target the field - the theme's focus.",
   ["4 fields", "On-theme generation", "Pet hashtags on demand", "Monday hashtags on demand"]),
 S("hh-seed", "The Seed Promise", "Craft",
   "Same seed, same hashtag - the style, twist, and sub-picks are all deterministic.",
   "Mulberry32 PRNG drives every pick.",
   "Parity-tested at build time.",
   "The Signature reading: the seed decides. Deterministic hashtags.",
   "Try the Signature method: keep the seed - the reproducible tag.",
   ["Same seed, same tag", "Every pick deterministic", "Mulberry32", "Reproducible"]),
 S("hh-use", "The Use Case", "Craft",
   "Hashtags are for posts, events, campaigns, and group chats. The generator names things worth gathering around.",
   "Naming is the use: the tag gathers the tribe.",
   "Posts, events, campaigns.",
   "The Signature reading: the tag gathers. Naming is the use.",
   "Try the Signature method: name the gathering - the tag's purpose.",
   ["Posts and events", "Campaigns", "Group chats", "Gathering around"]),
 S("hh-camel", "The CamelCase Rule", "Craft",
   "Every tag is CamelCase: readable, accessible, screen-reader friendly. #CozyCoffee, never #cozycoffee.",
   "CamelCase is the accessibility standard for multi-word hashtags.",
   "Enforced in every build.",
   "The Signature reading: the case is Camel. Readability enforced.",
   "Try the Signature method: capitalize each word - the accessible tag.",
   ["CamelCase always", "Screen-reader friendly", "Readability standard", "Enforced"]),
 S("hh-evolve", "The Evolution Habit", "Craft",
   "Take any tag and re-style it: #CozyCoffee becomes #CoffeeToffee. The re-style habit multiplies tags.",
   "One topic, eight styles: the remix exercise.",
   "The style-swap technique.",
   "The Signature reading: the re-style multiplies. Eight per topic.",
   "Try the Signature method: re-style it - the remix habit.",
   ["One topic, eight styles", "Re-style freely", "Remix exercise", "Multiply the tags"]),
 S("hh-archive", "The Archive Canon", "Craft",
   "34 seeded hashtags are the canon - the generator's greatest tags, fixed and scored.",
   "Seeded records anchor the range.",
   "34 canonical tags.",
   "The Signature reading: the canon anchors. Greatest tags, fixed.",
   "Try the Signature method: read the 34 - the canon of tags.",
   ["34 seeded tags", "Fixed and scored", "The canon", "Anchors the range"]),
 S("hh-signature", "The Signature Gear", "Craft",
   "The Signature edition compounds style and twist: the technique reinforces the topic's energy. Same engine, sharper.",
   "Signature = style-twist compounding.",
   "The sharper gear.",
   "The Signature reading: the gear is sharper. Technique compounds.",
   "Try the Signature method: shift sharper - the Signature tag.",
   ["Same engine", "Compounds harder", "Technique reinforces", "Sharper gear"]),
 S("hh-live", "The Live Engine", "Craft",
   "The generator runs in your browser - hashtags at the speed of thought, no server involved.",
   "Deterministic client-side JavaScript.",
   "Offline after load.",
   "The Signature reading: the tags are local. Speed of thought.",
   "Try the Signature method: generate locally - the instant tag.",
   ["Browser-native", "No server", "Instant", "Offline tags"]),
 S("hh-trend", "The Trend Test", "Craft",
   "Would you put it in your bio? The bio test is the hashtag's quality gate.",
   "Bio-worthiness as the metric.",
   "The bio test.",
   "The Signature reading: the bio decides. Worthiness is the gate.",
   "Try the Signature method: bio-test it - the quality gate.",
   ["Bio-worthiness", "The metric", "Quality gate", "Would you bio it?"]),
 S("hh-joy", "The Joy Standard", "Craft",
   "The standard is delight: if the tag doesn't make you smile, re-roll. The smile is the spec.",
   "Delight as acceptance criterion.",
   "The smile spec.",
   "The Signature reading: the smile is the spec. Delight decides.",
   "Try the Signature method: smile-test it - the acceptance.",
   ["Delight is standard", "Smile is spec", "Re-roll till it grins", "Acceptance: joy"]),
]

register({
    "slug": "gen-hashtag-idea-generator",
    "theme": "internet-humor",
    "first_pick": True,
    "name": "The Hashtag Idea Generator Database",
    "tagline": ("A real working hashtag generator: 8 style transforms, twist suffixes, length "
                "validation, and a computed shareability score."),
    "record_kind": "generated hashtag record",
    "pub_line": ("Public generator - a real client-side hashtag engine: pick a seed and field, "
                 "get a crafted hashtag with its technique and score."),
    "ai": "JAH Hashtag Engineer",
    "role": ("hashtag engineer - crafting hashtags with real transforms; answering from many "
             "angles - the topic, the style, the score - using only archive data"),
    "search_ph": "Search the hashtag canon...",
    "chat_ph": "Give me a seed - I will tag it...",
    "fields": FIELDS,
    "gen_desc": ("Generate REAL hashtags with the live client-side engine. Seeded archive "
                 "records are the authoritative entries."),
    "greet": "Give me any seed number - I will tag it brilliantly.",
    "gen_kind": "hashtag",
    "citation": CITE,
    "demo_default": "report",
    "seeds": SEEDS,
    "custom_records": custom_records,
    "gen_js": gen_js,
})
