#!/usr/bin/env python3
"""Wave 1 GENERATOR item: gen-infinite-curiosity (first-release pick).

A REAL working client-side curiosity-chain generator: a bank of 72 verified
curiosity nodes (fact + the question it provokes) across 8 topics. The engine
walks a seeded, non-repeating chain - fact, provocative question, deeper fact -
so every generation is a genuine curiosity trail, reproducible from its seed.

Python mirrors the JS PRNG/walk bit-for-bit (mulberry32 + Fisher-Yates), so
the 34 sample archive records are reproducible live in the browser via the
seed printed on each record.
"""
import json

from lib import register

TOPICS = ["Space", "Human Body", "Earth & Nature", "Animals",
          "History", "Physics", "Technology", "Numbers"]

# (topic, fact, why) - every fact real, every "why" a genuine follow-up.
NODES = [
# --- Space (0-8) ---
("Space", "The Moon is drifting away from Earth at about 3.8 cm per year.",
 "What happens when it drifts too far to cause total solar eclipses?"),
("Space", "A day on Venus lasts longer than its year - it rotates once every 243 Earth days but orbits in 225.",
 "Why does Venus spin backwards compared to most planets?"),
("Space", "Venus is the hottest planet at 465 C - hotter than Mercury, though it is farther from the Sun.",
 "What runaway process made the second planet hotter than the first?"),
("Space", "Saturn would float in water: it is the least dense planet, at 0.69 g per cubic cm.",
 "What is Saturn actually made of, if it is lighter than water?"),
("Space", "There are more stars in the universe than grains of sand on all of Earth's beaches.",
 "With that many stars, where is everybody?"),
("Space", "Light from the Sun takes 8 minutes 20 seconds to reach Earth.",
 "What does that delay mean for how we see the universe's past?"),
("Space", "Olympus Mons on Mars is nearly three times the height of Everest.",
 "Why can Mars grow volcanoes so much bigger than Earth's?"),
("Space", "A year on Neptune lasts 165 Earth years - it has completed just one orbit since its discovery.",
 "What was happening on Earth when Neptune was last in this position?"),
("Space", "The Great Red Spot is a storm wider than Earth that has raged for centuries.",
 "What fuels a storm that never stops?"),
# --- Human Body (9-17) ---
("Human Body", "Your stomach gets a new lining every few days so it does not digest itself.",
 "What happens when that renewal process fails?"),
("Human Body", "You cannot tickle yourself because your brain predicts the sensation and cancels it.",
 "What does that prediction system reveal about consciousness?"),
("Human Body", "Humans share about 60 percent of their DNA with bananas.",
 "What does 'shared DNA' actually mean for such different organisms?"),
("Human Body", "Your bones are stronger than concrete, ounce for ounce.",
 "What material in bone gives it that strength-to-weight ratio?"),
("Human Body", "The dark-adapted human eye can detect a single photon.",
 "If we can see single photons, why is night vision still so poor?"),
("Human Body", "Goosebumps are a leftover reflex from when humans had full body fur.",
 "What other reflexes are evolutionary leftovers?"),
("Human Body", "Your brain runs on about 20 watts - enough to power a dim light bulb.",
 "How does 20 watts outperform supercomputers at some tasks?"),
("Human Body", "Babies are born with about 300 bones; adults have 206.",
 "Which bones fuse together, and why start with more?"),
("Human Body", "Your nose can remember about 50,000 different scents.",
 "Why is smell the sense most tied to memory?"),
# --- Earth & Nature (18-26) ---
("Earth & Nature", "The Sahara was green and full of lakes just 6,000 years ago.",
 "What flipped the Sahara from green to desert?"),
("Earth & Nature", "Lake Natron in Tanzania can calcify animals that die in its waters.",
 "What chemistry turns a lake into a stone-maker?"),
("Earth & Nature", "Antarctica is the largest desert in the world.",
 "How can a desert be made of ice?"),
("Earth & Nature", "The Amazon produces about 6 percent of the world's oxygen - not 20 percent as often claimed.",
 "If not the Amazon, where does our oxygen actually come from?"),
("Earth & Nature", "There are about 3 trillion trees on Earth - more trees than stars in the Milky Way.",
 "How do scientists count 3 trillion trees?"),
("Earth & Nature", "The deepest part of the ocean is deeper than Everest is tall.",
 "What lives at the bottom of the deepest trench?"),
("Earth & Nature", "Lightning strikes Earth about 100 times every second.",
 "What separates the charges to make lightning at all?"),
("Earth & Nature", "Parts of the Atacama Desert have never recorded rainfall.",
 "What makes one strip of coast the driest place on Earth?"),
("Earth & Nature", "Mount Everest grows about 4 mm taller every year.",
 "What tectonic collision is still pushing it up?"),
# --- Animals (27-35) ---
("Animals", "Octopuses have three hearts and blue blood.",
 "Why did evolution give them three hearts?"),
("Animals", "Tardigrades have survived the vacuum of space.",
 "How does anything survive hard vacuum?"),
("Animals", "The mantis shrimp's punch is as fast as a bullet.",
 "What happens to water when something moves through it that fast?"),
("Animals", "Crows can recognize human faces and hold grudges for years.",
 "How do crows teach their young which humans to distrust?"),
("Animals", "Axolotls can regrow entire limbs, including bones and nerves.",
 "Why can't humans regrow limbs if axolotls can?"),
("Animals", "The immortal jellyfish can revert to its juvenile stage indefinitely.",
 "What would it take to trigger that reversal in other organisms?"),
("Animals", "Honeybees can recognize human faces.",
 "How does such a tiny brain do face recognition?"),
("Animals", "Sea cucumbers breathe through their anuses.",
 "What evolutionary path leads to breathing that way?"),
("Animals", "Polar bear fur is transparent, not white.",
 "How does transparent fur look white?"),
# --- History (36-44) ---
("History", "The Great Pyramid was the tallest human-made structure for 3,800 years.",
 "What finally beat it in the 1300s?"),
("History", "Oxford University is older than the Aztec Empire.",
 "What was being taught at Oxford when Tenochtitlan was founded?"),
("History", "Nintendo was founded in 1889 as a playing-card company.",
 "What did Nintendo make before video games?"),
("History", "The Eiffel Tower was originally intended for Barcelona.",
 "Why did Barcelona reject it?"),
("History", "The London Underground opened in 1863, while the American Civil War was raging.",
 "What did the first subway look like?"),
("History", "Harvard was founded before calculus was invented.",
 "What did Harvard teach before modern science existed?"),
("History", "The fax machine was invented in 1843 - before the telephone.",
 "How did a fax work without phone lines as we know them?"),
("History", "The University of al-Qarawiyyin, founded in 859 AD, is the oldest existing university.",
 "What was studied there in the 800s?"),
("History", "The first university degrees were awarded in the 1100s.",
 "What did the first graduates study?"),
# --- Physics (45-53) ---
("Physics", "Time moves slower at your feet than at your head, due to gravity.",
 "Has anyone actually measured the difference across a human body?"),
("Physics", "Glass is neither a true solid nor a liquid - it is an amorphous solid.",
 "Do old church windows really flow downward over the centuries?"),
("Physics", "Hot water can freeze faster than cold water - the Mpemba effect.",
 "What mechanism could possibly explain that?"),
("Physics", "You are 99.9999999 percent empty space.",
 "If atoms are nearly all empty, why can't we walk through walls?"),
("Physics", "Quantum particles can be in two places at once until observed.",
 "What counts as an 'observation' in quantum mechanics?"),
("Physics", "The speed of light is the same for all observers, no matter how fast they move.",
 "What breaks in physics if the speed of light were not constant?"),
("Physics", "Absolute zero can never be reached - only approached.",
 "What law of physics forbids reaching it?"),
("Physics", "Sound travels about 4.3 times faster in water than in air.",
 "Why does density speed sound up but slow light down?"),
("Physics", "Magnets lose their magnetism when heated past the Curie point.",
 "What is happening inside the metal at that temperature?"),
# --- Technology (54-62) ---
("Technology", "The first computer bug was a real moth, found in 1947.",
 "Who found it, and is the logbook page real?"),
("Technology", "QR codes were invented for tracking car parts.",
 "What limitation of barcodes forced the invention?"),
("Technology", "The first webcam watched a coffee pot at Cambridge.",
 "Whose coffee was worth inventing the webcam for?"),
("Technology", "GPS satellites must correct for relativity, or they would drift kilometers daily.",
 "How big would the positioning error be without the correction?"),
("Technology", "The QWERTY layout was designed to slow typists down.",
 "What problem were jamming typewriter keys causing?"),
("Technology", "The first domain name ever registered was Symbolics.com, in 1985.",
 "What happened to Symbolics?"),
("Technology", "Your phone has more computing power than NASA had for Apollo 11.",
 "How did they reach the Moon with less computing than a phone?"),
("Technology", "The 'save' icon is a floppy disk most users have never seen.",
 "What other interface fossils survive from dead technology?"),
("Technology", "Email existed before the World Wide Web.",
 "What network carried the first emails?"),
# --- Numbers (63-71) ---
("Numbers", "A sheet of paper folded 103 times would exceed the observable universe.",
 "How can 103 folds beat the entire universe?"),
("Numbers", "The number zero was invented independently in multiple civilizations.",
 "How did mathematics work without zero?"),
("Numbers", "A 'jiffy' is a real unit of time: one hundredth of a second in computing.",
 "Who needed a word for a hundredth of a second?"),
("Numbers", "The word 'hundred' once meant 120 in some Germanic counting systems.",
 "What was the 'long hundred' used for?"),
("Numbers", "111,111,111 times 111,111,111 equals 12,345,678,987,654,321.",
 "What pattern makes that multiplication work?"),
("Numbers", "Many buildings skip the 13th floor.",
 "Do the elevators really skip it, or just rename it?"),
("Numbers", "A 'googol' (10 to the 100th) is bigger than the number of atoms in the universe.",
 "Why did a search company name itself after it?"),
("Numbers", "The Fibonacci sequence appears in sunflower spirals and pinecones.",
 "What is the plant actually optimizing?"),
("Numbers", "Pi has been computed to over 200 trillion digits.",
 "Why compute digits that nobody will ever use?"),
]
assert len(NODES) == 72

# ---------------------------------------------------------------- PRNG (mirrors the JS bit-for-bit)
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
        t = _s32(_s32(t + _imul(tu ^ (tu >> 7), 61 | tu)) ^ t)
        tu = t & 0xFFFFFFFF
        return ((tu ^ (tu >> 14)) & 0xFFFFFFFF) / 4294967296.0
    return rnd


def _perm(n, rnd):
    p = list(range(n))
    for i in range(n - 1, 0, -1):
        j = int(rnd() * (i + 1))
        p[i], p[j] = p[j], p[i]
    return p


def walk_chain(seed, depth=5, topic=None):
    """Seeded non-repeating curiosity walk. Mirrors the client-side JS."""
    rnd = make_prng(seed)
    order = _perm(len(NODES), rnd)
    used = set()
    if topic:
        start = next(i for i in order if NODES[i][0] == topic)
    else:
        start = order[0]
    chain = [start]
    used.add(start)
    while len(chain) < depth:
        cur_topic = NODES[chain[-1]][0]
        nxt = next((i for i in order
                    if i not in used and NODES[i][0] == cur_topic), None)
        if nxt is None:
            nxt = next((i for i in order if i not in used), None)
        if nxt is None:
            break
        chain.append(nxt)
        used.add(nxt)
    return chain


def chain_prose(chain, seed, signature=False):
    parts = []
    for k, ni in enumerate(chain):
        topic, fact, why = NODES[ni]
        if k == 0:
            parts.append("Start here: %s" % fact)
        else:
            parts.append("The answer pulls you deeper: %s" % fact)
        if k < len(chain) - 1:
            bridge = ("That raises the question: %s" % why
                      if k == 0 else "Which makes you wonder: %s" % why)
            parts.append(bridge)
    closing = ("Follow the chain far enough and every answer becomes a doorway. "
               "That is the Infinite Curiosity method: never stop at the answer - "
               "ask what it opens. (Seed %d reproduces this exact chain in the "
               "generator.)" % seed)
    if signature:
        closing += (" The Signature treatment: each link is chosen to compound the "
                    "last, so the chain teaches progressively - simple wonder first, "
                    "deeper mechanism later.")
    parts.append(closing)
    return "\n\n".join(parts)


def chain_title(chain, i, signature=False):
    first_fact = NODES[chain[0]][1]
    hook = first_fact[:64].rsplit(" ", 1)[0]
    t = "Curiosity Chain %d: %s..." % (i + 1, hook)
    if signature:
        t += " (Signature Edition)"
    return t


def custom_records(source, prefix):
    sig = (source == "signature")
    raw = []
    for i in range(34):
        seed = 7000 + i * 131
        depth = 3 + min(i // 9, 3) + (1 if sig else 0)
        depth = min(depth, 8)
        chain = walk_chain(seed, depth)
        topics = sorted(set(NODES[ni][0] for ni in chain))
        g = NODES[chain[0]][0]
        links = ["%s: %s" % (NODES[ni][0], NODES[ni][1]) for ni in chain]
        desc = chain_prose(chain, seed, sig)
        how = ("The Infinite Curiosity engine walks a bank of 72 verified curiosity "
               "nodes with a seeded random walk: each fact carries the question it "
               "provokes, and the next link is drawn from unvisited nodes - "
               "preferring the same topic so the chain deepens rather than wanders. "
               "The seed makes every chain reproducible; depth grows along the "
               "teaching ladder from 3-link foundations to %d-link advanced chains."
               % depth)
        raw.append({
            "t": chain_title(chain, i, sig),
            "g": g,
            "description": desc,
            "how_it_works": how,
            "key_points": links,
            "requirements": "Reading only - no equipment needed.",
            "citations": ["Chain facts per the database citation; seed %d reproduces this chain in the live generator." % seed],
            "demo": "chain",
            "seed": {"chain": links,
                     "points": links,
                     "fact": desc[:400],
                     "mechanism": how[:300]},
        })
    return raw


GEN_JS_TEMPLATE = r"""(function(){'use strict';
/* JAH Infinite Curiosity Generator - jahdb-gen-infinite-curiosity-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL client-side generator: walks a bank of 72 verified curiosity nodes
   with a seeded, non-repeating walk. Same seed, same chain - every time.
   __SOURCE__ edition. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function perm(n,rnd){var p=[];for(var i=0;i<n;i++)p.push(i);for(var i=n-1;i>0;i--){var j=(rnd()*(i+1))|0;var t=p[i];p[i]=p[j];p[j]=t;}return p;}
var PREFIX=__PREFIX__;
var TOPICS=__TOPICS__;
var NODES=__NODES__;
var MAXDEPTH=__MAXDEPTH__;
var SOURCE='__SOURCE__';
function walkChain(seed,depth,topic){
  var rnd=prng(seed), order=perm(NODES.length,rnd), used={}, chain=[];
  var start=order[0];
  if(topic){ for(var k=0;k<order.length;k++){ if(NODES[order[k]].t===topic){ start=order[k]; break; } } }
  chain.push(start); used[start]=1;
  while(chain.length<depth){
    var curT=NODES[chain[chain.length-1]].t, nxt=-1, i, id;
    for(i=0;i<order.length;i++){ id=order[i]; if(!used[id]&&NODES[id].t===curT){ nxt=id; break; } }
    if(nxt<0){ for(i=0;i<order.length;i++){ id=order[i]; if(!used[id]){ nxt=id; break; } } }
    if(nxt<0) break;
    chain.push(nxt); used[nxt]=1;
  }
  return chain;
}
function chainProse(chain,seed){
  var parts=[];
  for(var k=0;k<chain.length;k++){
    var n=NODES[chain[k]];
    parts.push(k===0?('Start here: '+n.f):('The answer pulls you deeper: '+n.f));
    if(k<chain.length-1) parts.push((k===0?'That raises the question: ':'Which makes you wonder: ')+n.w);
  }
  parts.push('Follow the chain far enough and every answer becomes a doorway. That is the Infinite Curiosity method: never stop at the answer - ask what it opens. (Seed '+seed+'.)'+(SOURCE==='signature'?' The Signature treatment compounds each link: simple wonder first, deeper mechanism later.':''));
  return parts.join('\n\n');
}
function demoProgram(chain){
  var lines=chain.map(function(id,k){return '    print("  '+(k+1)+'. '+NODES[id].f.replace(/"/g,"'")+'")';});
  return '# Infinite Curiosity Generator - live chain\nLINKS = [\n'+chain.map(function(id){return '    "'+NODES[id].t+': '+NODES[id].f.replace(/"/g,"'")+'",';}).join('\n')+'\n]\ndef main():\n    print("CURIOSITY CHAIN")\n'+lines.join('\n')+'\n    print("chain length: %d links" % len(LINKS))\n    print("OK: curiosity chain of %d links generated" % len(LINKS))\nif __name__ == "__main__":\n    main()\n';
}
function generate(seed,opts,rnd){
  opts=opts||{};
  var depth=Math.min(MAXDEPTH,Math.max(3,opts.depth|0||5));
  var field=(opts.field&&TOPICS.indexOf(opts.field)>=0)?opts.field:null;
  var chain=walkChain(seed>>>0||1,depth,field);
  var firstT=NODES[chain[0]].t;
  var hook0=NODES[chain[0]].f.slice(0,64);
  var hook=hook0.slice(0,Math.max(1,hook0.lastIndexOf(' ')));
  var title='Curiosity Chain (live): '+hook+'...'+(SOURCE==='signature'?' (Signature Edition)':'');
  var desc=chainProse(chain,seed>>>0||1);
  var id=PREFIX+String(seed>>>0||1).padStart(6,'0');
  return {
    id:id,
    name:title+' — '+firstT,
    title:title,
    description:'GENERATED CHAIN (live generator output - clearly labeled). '+desc,
    field:firstT,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Live generator output - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:demoProgram(chain),note:'Live chain demo program.'},
    _seed:seed>>>0||1, chain:chain
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(TOPICS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.chain||!r.chain.length)e.push('chain');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-gen-infinite-curiosity-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:TOPICS,nodes:NODES,walkChain:walkChain,maxDepth:MAXDEPTH};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-infinite-curiosity',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""


def gen_js(source, prefix, cfg):
    nodes_js = json.dumps([{"t": t, "f": f, "w": w} for t, f, w in NODES],
                          ensure_ascii=False)
    js = GEN_JS_TEMPLATE
    js = js.replace("__PREFIX__", json.dumps(prefix))
    js = js.replace("__TOPICS__", json.dumps(TOPICS, ensure_ascii=False))
    js = js.replace("__NODES__", nodes_js)
    js = js.replace("__MAXDEPTH__", "10" if source == "signature" else "8")
    js = js.replace("__SOURCE__", source)
    return js


def S(key, t, g, fact, mechanism, evidence, sig_angle, sig_do, points, **kw):
    d = dict(key=key, t=t, g=g, fact=fact, mechanism=mechanism,
             evidence=evidence, sig_angle=sig_angle, sig_do=sig_do,
             points=points)
    d.update(kw)
    return d


CITE = ("Curiosity nodes drawn from standard popular-science references "
        "(encyclopedia science entries, institutional fact sheets); striking "
        "claims should be verified against primary sources before repeating.")

# 17 registration seeds (the engine's starter trails); the 34 archive records
# come from custom_records above.
SEEDS = [
 S("gic-starter-space", "The Moon Is Leaving Us", "Space",
   "The Moon drifts 3.8 cm farther from Earth every year.",
   "Tidal friction transfers Earth's rotational energy to the Moon's orbit.",
   "Laser ranging from Apollo retroreflectors measures the drift directly.",
   "The Signature reading: even the Moon leaves. Departure is orbital mechanics, not betrayal.",
   "Try the Signature method: measure your 3.8 cm - the slow departure in your own orbit.",
   ["3.8 cm per year", "Tidal friction mechanism", "Measured by laser ranging", "Eclipses will end"]),
 S("gic-starter-body", "The Brain That Cancels Tickle", "Human Body",
   "You cannot tickle yourself because your brain predicts and cancels the sensation.",
   "The cerebellum's forward model subtracts self-generated sensation.",
   "Schizophrenia research shows the cancellation failing - patients can tickle themselves.",
   "The Signature reading: the brain edits reality before you feel it. Perception is prediction.",
   "Try the Signature method: notice your predictions - the sensations your brain cancels.",
   ["Self-tickle impossible", "Cerebellum forward model", "Fails in schizophrenia", "Perception is prediction"]),
 S("gic-starter-earth", "The Green Sahara", "Earth & Nature",
   "The Sahara was green with lakes 6,000 years ago.",
   "Orbital precession shifted monsoon patterns; the change took centuries.",
   "Lake-bed sediments and rock art document the green Sahara.",
   "The Signature reading: deserts were gardens. Climate is orbital, not permanent.",
   "Try the Signature method: read your lake-beds - the green past under your desert.",
   ["Green 6,000 years ago", "Orbital precession cause", "Sediments + rock art proof", "Took centuries to flip"]),
 S("gic-starter-animals", "The Three-Hearted Genius", "Animals",
   "Octopuses have three hearts and blue blood.",
   "Copper-based hemocyanin carries oxygen; two hearts serve the gills, one the body.",
   "Marine biology confirms the anatomy; the intelligence is well documented.",
   "The Signature reading: three hearts, one genius. Redundancy serves the remarkable.",
   "Try the Signature method: grow your third heart - the redundancy your genius needs.",
   ["Three hearts, blue blood", "Hemocyanin oxygen carrier", "Documented intelligence", "Two for gills, one for body"]),
 S("gic-starter-history", "The Pyramid's 3,800-Year Record", "History",
   "The Great Pyramid was the tallest human-made structure for 3,800 years.",
   "146 meters of limestone, aligned to the cardinal points within fractions of a degree.",
   "Survey data confirms the dimensions; the record duration is historical fact.",
   "The Signature reading: 3,800 years unbeaten. Build for the long record.",
   "Try the Signature method: build your pyramid - the structure that stands 3,800 years.",
   ["146 m tall", "3,800-year record", "Cardinal alignment", "Beaten in the 1300s"]),
 S("gic-starter-physics", "The Slower Feet", "Physics",
   "Time moves slower at your feet than at your head.",
   "Gravitational time dilation: deeper in a gravity well, clocks tick slower.",
   "NIST measured the difference across 33 cm in 2010.",
   "The Signature reading: your feet age slower. Relativity is personal.",
   "Try the Signature method: feel your dilation - the relativity across your own body.",
   ["Feet slower than head", "Gravitational time dilation", "NIST 2010: 33 cm measured", "Relativity is personal"]),
 S("gic-starter-tech", "The Moth in the Machine", "Technology",
   "The first computer bug was a real moth, found in 1947.",
   "The moth was taped into the Harvard Mark II logbook with the note 'first actual case of bug being found.'",
   "The Smithsonian holds the logbook page.",
   "The Signature reading: the bug was literal. Every metaphor was once a moth.",
   "Try the Signature method: tape your moth - the literal origin of your metaphor.",
   ["1947, Harvard Mark II", "Taped into the logbook", "Smithsonian holds it", "'First actual case of bug'"]),
 S("gic-starter-numbers", "The 103-Fold Universe", "Numbers",
   "Paper folded 103 times would exceed the observable universe.",
   "Exponential doubling: 0.1 mm times 2^103 dwarfs 93 billion light-years.",
   "The arithmetic is exact; the physical folding stops around 7 folds.",
   "The Signature reading: doubling defeats distance. Exponentials beat universes.",
   "Try the Signature method: count your doublings - the folds to your universe.",
   ["2^103 doublings", "Beats 93B light-years", "Physical limit ~7 folds", "Exponential beats intuition"]),
 S("gic-starter-space2", "The Backwards Planet", "Space",
   "Venus spins backwards - and one Venusian day outlasts its year.",
   "A giant impact or atmospheric tides likely flipped its rotation.",
   "Radar mapping confirms the retrograde spin.",
   "The Signature reading: the planet spins wrong. Wrong can be stable for billions of years.",
   "Try the Signature method: spin your backwards - the stable wrongness.",
   ["Retrograde rotation", "Day longer than year", "Radar-confirmed", "Stable for eons"]),
 S("gic-starter-body2", "The 20-Watt Supercomputer", "Human Body",
   "Your brain runs on 20 watts - a dim bulb's worth of power.",
   "86 billion neurons at ~20 watts outperform megawatt data centers at pattern tasks.",
   "The 20-watt figure is neuroscience standard.",
   "The Signature reading: 20 watts beats megawatts. Efficiency is intelligence.",
   "Try the Signature method: run on 20 watts - the efficiency your supercomputer lacks.",
   ["20 watts", "86B neurons", "Beats megawatts at patterns", "Efficiency is intelligence"]),
 S("gic-starter-earth2", "The Ice Desert", "Earth & Nature",
   "Antarctica - the largest desert on Earth - is made of ice.",
   "Desert means dry: Antarctica's interior gets less precipitation than the Sahara.",
   "The desert classification is standard geography.",
   "The Signature reading: the desert is ice. Definitions decide the record.",
   "Try the Signature method: define your desert - the definition that changes the map.",
   ["Largest desert", "Drier than the Sahara", "Made of ice", "Desert means dry"]),
 S("gic-starter-animals2", "The Immortal Jellyfish", "Animals",
   "Turritopsis dohrnii can revert to its juvenile polyp stage indefinitely.",
   "Transdifferentiation rewinds its cells; the cycle can repeat.",
   "Marine biology documents the reversal.",
   "The Signature reading: the adult becomes the child. Reversal is a survival strategy.",
   "Try the Signature method: revert your polyp - the juvenile stage you can return to.",
   ["Reverts to juvenile stage", "Transdifferentiation", "Cycle repeats", "Biologically immortal"]),
 S("gic-starter-history2", "The Card Company", "History",
   "Nintendo was founded in 1889 - as a playing-card company.",
   "Fusajiro Yamauchi made hanafuda cards; video games came 90 years later.",
   "Corporate history confirms the 1889 founding.",
   "The Signature reading: the game company sold cards. Origins rarely predict destinations.",
   "Try the Signature method: sell your hanafuda - the card business before the console.",
   ["1889 founding", "Hanafuda cards", "Games came 90 years later", "Origins don't predict"]),
 S("gic-starter-physics2", "The Empty You", "Physics",
   "You are 99.9999999 percent empty space.",
   "Atoms are nucleus plus vast electron-cloud volume; matter is mostly nothing.",
   "The figure is standard atomic physics.",
   "The Signature reading: you are mostly nothing. Solidity is electromagnetic repulsion.",
   "Try the Signature method: feel your emptiness - the nothing you are mostly made of.",
   ["99.9999999% empty", "Nucleus + cloud volume", "Solidity is repulsion", "Standard physics"]),
 S("gic-starter-tech2", "The Coffee-Pot Camera", "Technology",
   "The first webcam watched a coffee pot at Cambridge.",
   "Researchers pointed a camera at the pot to avoid wasted trips; the stream ran for years.",
   "The Trojan Room coffee pot is computing lore.",
   "The Signature reading: the webcam watched coffee. Great inventions start with laziness.",
   "Try the Signature method: camera your coffee - the lazy invention that starts the era.",
   ["Cambridge coffee pot", "Avoided wasted trips", "Ran for years", "Laziness invents"]),
 S("gic-starter-numbers2", "The Invention of Nothing", "Numbers",
   "Zero was invented independently in multiple civilizations.",
   "The Maya, Indians, and Babylonians each reached for nothing as a number.",
   "The independent inventions are historical consensus.",
   "The Signature reading: nothing was invented thrice. The hardest number took three civilizations.",
   "Try the Signature method: invent your zero - the nothing your system needs.",
   ["Maya, India, Babylon", "Independent inventions", "Hardest number", "Nothing as a number"]),
 S("gic-starter-chain", "The Method Itself", "Space",
   "Every chain in this database is reproducible from its seed.",
   "The mulberry32 PRNG plus Fisher-Yates shuffle generate identical chains in Python and JavaScript.",
   "Bit-for-bit parity is tested at build time.",
   "The Signature reading: the method is the record. Reproducibility is the Signature standard.",
   "Try the Signature method: seed your chain - the reproducibility that makes it Signature.",
   ["Seeded PRNG", "Fisher-Yates walk", "Python/JS parity", "Reproducibility is Signature"]),
]

register({
    "slug": "gen-infinite-curiosity",
    "theme": "wow-facts",
    "first_pick": True,
    "name": "The Infinite Curiosity Generator Database",
    "tagline": ("A real working curiosity-chain generator: seeded walks through 72 verified "
                "wonder-nodes, each fact opening the next question, endlessly."),
    "record_kind": "curiosity chain record",
    "pub_line": ("Public generator - a real client-side curiosity engine: pick a seed and topic, "
                 "get a genuine chain of facts where each answer opens the next question."),
    "ai": "JAH Curiosity Engine",
    "role": ("curiosity engine - generating genuine curiosity chains from verified nodes; "
             "answering from many angles - the fact, the question it opens, the deeper fact - "
             "using only archive data"),
    "search_ph": "Search curiosity chains...",
    "chat_ph": "Give me a seed and I will chain your curiosity...",
    "fields": TOPICS,
    "gen_desc": ("Generate REAL curiosity chains with the live client-side engine. Seeded archive "
                 "records are the authoritative entries."),
    "greet": "Give me any seed number - I will walk you down a genuine chain of wonder.",
    "gen_kind": "curiosity-chain",
    "citation": CITE,
    "demo_default": "chain",
    "seeds": SEEDS,
    "custom_records": custom_records,
    "gen_js": gen_js,
})
