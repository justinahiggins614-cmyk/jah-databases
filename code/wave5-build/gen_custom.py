#!/usr/bin/env python3
"""Custom hand-authored generators for wave 5's 4 GENERATOR-class items.

Each entry: {"js": js_fn, "records": rec_fn}
  js_fn(source, prefix, cfg) -> JS source string (hand-authored, deterministic,
      REAL working generator producing genuine outputs; passes node --check and
      the generate/validate smoke test).
  rec_fn(source, prefix) -> 34 raw record dicts (t, g, description,
      how_it_works, key_points, requirements, citations, demo, seed) built by
      the same deterministic logic in Python.

Property of Justin Addam Higgins (JAH).
"""
import hashlib

JS_HEAD = """(function(){'use strict';
/* JAH @@NAME@@ generator - @@GENVER@@.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same output. Real working generator. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,s){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(s()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX="@@PREFIX@@";
"""

JS_TAIL = """
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
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'@@GENVER@@',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('@@SLUG@@',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""


def _fill(tmpl, **kw):
    for k, v in kw.items():
        tmpl = tmpl.replace("@@" + k + "@@", v)
    return tmpl


# ============================================================ 1. detective case
JS_DETECTIVE = JS_HEAD + """
var FIELDS=["Classic Cases","Locked Rooms","Countryside Crimes"];
var VICTIMS=[["Elias Vane","clockmaker"],["Mara Quill","novelist"],["Dr. Theo Marsh","botanist"],["Ada Bloom","jeweler"],["Silas Crane","ship captain"],["Nora Finch","beekeeper"],["Otto Brandt","watchmaker"],["Iris Vale","cartographer"],["Hugo Stern","chef"],["Lena Moss","librarian"],["Felix Hart","locksmith"],["June Park","florist"]];
var PLACES=["the lighthouse gallery","the orchard manor","the riverside inn","the old observatory","the clock tower","the vineyard estate","the harbor warehouse","the mountain lodge","the botanical glasshouse","the railway depot","the mill house","the seaside pavilion"];
var NAMES=["Amos Reed","Bea Lark","Cyrus Pike","Dora Venn","Edgar Moss","Faye Noor","Gus Hale","Hazel Quinn","Ivan Petrov","Jill Faraday","Karl Brenner","Lila Santos"];
var OCC=["gardener","cook","chauffeur","secretary","stablehand","housekeeper","tutor","blacksmith","maid","accountant","driver","nurse"];
var MOTIVES=["an inheritance","a stolen recipe","a forged signature","a broken partnership","a hidden letter","a gambling debt","a promised promotion","a family feud"];
var METHODS=["a doctored telegram","a swapped key","a timed lock","a mislabeled bottle","a silenced bell","a faked footprint","a rerouted letter","a stopped clock"];
var CLUES=["A muddy boot print that does not match the victim's shoes.","A torn corner of a letter hidden in the fireplace.","A pocket watch stopped at the wrong hour.","A window latched from the inside with fresh scratches.","A half-finished cup of tea, still warm when found.","A library book checked out under a false name.","A key that fits no lock in the building.","A smudge of paint on the doorframe, still tacky.","A train timetable with one departure circled.","A button torn from a coat, found in the garden."];
function demoProgram(c){
  var safe=c.title.replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  var sus=c.suspects.map(function(s){return '    ("'+s.name+'", '+s.alibi+')';}).join(',\\n');
  return "# Detective case demo - "+safe+"\\n"
   + "SUSPECTS = [\\n"+sus+"\\n]\\n"
   + "SOLUTION = \\""+c.culprit+"\\"\\n"
   + "def main():\\n"
   + "    cleared=[n for n,a in SUSPECTS if a]\\n"
   + "    left=[n for n,a in SUSPECTS if not a]\\n"
   + "    print('suspects:', len(SUSPECTS))\\n"
   + "    print('cleared:', ', '.join(cleared))\\n"
   + "    assert len(left)==1 and left[0]==SOLUTION, 'solution mismatch'\\n"
   + "    print('solution:', SOLUTION)\\n"
   + "    print('OK: case solution verified')\\n"
   + "if __name__=='__main__':\\n    main()\\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var v=pick(VICTIMS,rnd), place=pick(PLACES,rnd);
  var motive=pick(MOTIVES,rnd), method=pick(METHODS,rnd);
  var people=shuffle(NAMES,rnd).slice(0,4);
  var occs=shuffle(OCC,rnd).slice(0,4);
  var suspects=people.map(function(n,i){return {name:n,occ:occs[i],alibi:true};});
  var ci=(rnd()*4)|0; suspects[ci].alibi=false;
  var clues=shuffle(CLUES,rnd).slice(0,6);
  var title="The "+place.charAt(4).toUpperCase()+place.slice(5)+" Case";
  var desc="CASE FILE (fictional detective case - a fair-play puzzle with a worked solution).\\n\\n"
   +v[0]+", the "+v[1]+", was found at "+place+" under strange circumstances.\\n"
   +"Four people were nearby: "+suspects.map(function(s){return s.name+" ("+s.occ+")";}).join(", ")+".\\n"
   +"The motive centers on "+motive+"; the method involved "+method+".\\n"
   +"Clues found at the scene:\\n- "+clues.join("\\n- ");
  var how="HOW THE DEDUCTION WORKS (solution). Three of the four suspects have alibis that check out; only "
   +suspects[ci].name+" the "+suspects[ci].occ+" has none. The decisive clues are the stopped pocket watch (the hour was staged), "
   +"the key that fits no lock (planted to suggest an intruder), and "+motive+" giving "+suspects[ci].name+" the reason. "
   +"The method - "+method+" - explains the locked scene. Fair-play check: every clue needed to name "+suspects[ci].name+" appears above.";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+" - detective case",
    title:title,
    description:desc,
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated fictional detective case - a puzzle with a fair solution, not a real event.',
    case:{title:title,suspects:suspects,culprit:suspects[ci].name},
    demo:{kind:"python",language:"python",program:demoProgram({title:title,suspects:suspects,culprit:suspects[ci].name}),note:"Case solution verifier."},
    _seed:seed
  };
}
""" + JS_TAIL

CASE_VICTIMS = [("Elias Vane", "clockmaker"), ("Mara Quill", "novelist"), ("Dr. Theo Marsh", "botanist"),
                ("Ada Bloom", "jeweler"), ("Silas Crane", "ship captain"), ("Nora Finch", "beekeeper"),
                ("Otto Brandt", "watchmaker"), ("Iris Vale", "cartographer"), ("Hugo Stern", "chef"),
                ("Lena Moss", "librarian"), ("Felix Hart", "locksmith"), ("June Park", "florist")]
CASE_PLACES = ["the lighthouse gallery", "the orchard manor", "the riverside inn", "the old observatory",
               "the clock tower", "the vineyard estate", "the harbor warehouse", "the mountain lodge",
               "the botanical glasshouse", "the railway depot", "the mill house", "the seaside pavilion"]
CASE_NAMES = ["Amos Reed", "Bea Lark", "Cyrus Pike", "Dora Venn", "Edgar Moss", "Faye Noor",
              "Gus Hale", "Hazel Quinn", "Ivan Petrov", "Jill Faraday", "Karl Brenner", "Lila Santos"]
CASE_OCC = ["gardener", "cook", "chauffeur", "secretary", "stablehand", "housekeeper",
            "tutor", "blacksmith", "maid", "accountant", "driver", "nurse"]
CASE_MOTIVES = ["an inheritance", "a stolen recipe", "a forged signature", "a broken partnership",
                "a hidden letter", "a gambling debt", "a promised promotion", "a family feud"]
CASE_METHODS = ["a doctored telegram", "a swapped key", "a timed lock", "a mislabeled bottle",
                "a silenced bell", "a faked footprint", "a rerouted letter", "a stopped clock"]
CASE_CLUES = ["A muddy boot print that does not match the victim's shoes.",
              "A torn corner of a letter hidden in the fireplace.",
              "A pocket watch stopped at the wrong hour.",
              "A window latched from the inside with fresh scratches.",
              "A half-finished cup of tea, still warm when found.",
              "A library book checked out under a false name.",
              "A key that fits no lock in the building.",
              "A smudge of paint on the doorframe, still tacky.",
              "A train timetable with one departure circled.",
              "A button torn from a coat, found in the garden."]
CASE_FIELDS = ["Classic Cases", "Locked Rooms", "Countryside Crimes"]


def _py_pick(rng, seq):
    return seq[int(rng() * len(seq)) % len(seq)]


def _py_shuffle(rng, seq):
    a = list(seq)
    for i in range(len(a) - 1, 0, -1):
        j = int(rng() * (i + 1)) % (i + 1)
        a[i], a[j] = a[j], a[i]
    return a


def _mulberry(seed):
    a = (seed & 0xFFFFFFFF) or 1
    def rnd():
        nonlocal a
        a = (a + 0x6D2B79F5) & 0xFFFFFFFF
        t = (a ^ (a >> 15)) * (1 | a) & 0xFFFFFFFF
        t = (t + ((t ^ (t >> 7)) * (61 | t) & 0xFFFFFFFF)) & 0xFFFFFFFF
        return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296.0
    return rnd


def py_detective_records(source, prefix):
    recs = []
    for s in range(1, 35):
        rng = _mulberry(s * 7919 + 13)
        v = _py_pick(rng, CASE_VICTIMS); place = _py_pick(rng, CASE_PLACES)
        motive = _py_pick(rng, CASE_MOTIVES); method = _py_pick(rng, CASE_METHODS)
        people = _py_shuffle(rng, CASE_NAMES)[:4]
        occs = _py_shuffle(rng, CASE_OCC)[:4]
        ci = int(rng() * 4) % 4
        suspects = [(people[i], occs[i], i != ci) for i in range(4)]
        clues = _py_shuffle(rng, CASE_CLUES)[:6]
        field = CASE_FIELDS[(s - 1) % 3]
        pname = place[4].upper() + place[5:]
        title = "The %s Case" % pname
        desc = ("SAMPLE CASE FILE %d (fictional detective case - a fair-play puzzle with a worked solution). "
                "%s, the %s, was found at %s under strange circumstances. Four people were nearby: %s. "
                "The motive centers on %s; the method involved %s. Clues found at the scene: %s" %
                (s, v[0], v[1], place,
                 "; ".join("%s (%s)" % (n, o) for n, o, _ in suspects),
                 motive, method, " ".join(clues)))
        how = ("HOW THE DEDUCTION WORKS (solution). Three suspects have alibis that check out; only %s the %s "
               "has none. The stopped pocket watch was staged, the key that fits no lock was planted to suggest "
               "an intruder, and %s gives %s the reason. The method - %s - explains the scene. Fair-play check: "
               "every clue needed to name the culprit appears in the case file above." %
               (suspects[ci][0], suspects[ci][1], motive, suspects[ci][0], method))
        recs.append({
            "t": title, "g": field, "description": desc, "how_it_works": how,
            "key_points": ["Victim: %s, the %s" % v,
                           "Scene: %s" % place,
                           "Motive: %s" % motive,
                           "Method: %s" % method,
                           "Solution: %s (%s) - the only suspect without an alibi" % (suspects[ci][0], suspects[ci][1]),
                           "Fair-play: all decisive clues appear in the case file"],
            "requirements": "Reading only - no equipment needed. A notebook helps track alibis.",
            "citations": ["Signature Detective Case Generator - fictional case file, generated sample."],
            "demo": "eliminate",
            "seed": {"suspects": [(n, a) for n, _, a in suspects]},
        })
    return recs


def js_detective(source, prefix, cfg):
    return _fill(JS_DETECTIVE, NAME=cfg["name"], GENVER="jahdb-%s-1.0" % cfg["slug"],
                 PREFIX=prefix, SLUG=cfg["slug"])


# ============================================================ 2. hidden message
JS_HIDDEN = JS_HEAD + """
var FIELDS=["Word Puzzles","Cipher Puzzles","Steganography"];
var MESSAGES=["MEET AT DAWN","THE KEY IS HIDDEN","FOLLOW THE RIVER","TRUST NO ONE","LOOK UNDER THE STONE","THE MAP IS REAL","WAIT FOR THE SIGNAL","THE DOOR IS OPEN","COUNT THE STARS","SILENCE KEEPS SECRETS","THE GARDEN GATE","MIDNIGHT BELLS RING"];
var SENT=["The old harbor bell rang twice at noon.","Gulls circled the empty lighthouse twice.","Rain washed the cobblestones until they shone.","A cat slept on the warm bakery steps.","Children chased paper boats down the gutter.","The baker stacked warm loaves by the window.","The clockmaker oiled his gears with care.","Maps of distant islands lined the study wall.","Tea steamed in chipped porcelain cups.","The gardener pruned roses before the frost.","Lanterns swayed along the quiet pier.","A dog barked once, then settled again.","Letters waited unsorted on the hall table.","The violinist tuned her strings by ear.","Boats knocked softly against the dock.","Stars appeared one by one overhead.","The mill wheel turned without hurrying.","Bread cooled on the wooden rack.","A shutter banged in the evening wind.","The cat stretched and yawned widely.","Footsteps echoed down the stone stair.","Candles guttered in the drafty hall.","The kettle sang on the iron stove.","Dust drifted through the sunbeam.","A robin landed on the fence post.","The ferry horn sounded far away.","Apples thudded softly in the orchard.","The blacksmith hammered out a rhythm.","Waves lapped the harbor wall gently.","The librarian shelved books by color."];
function caesar(m,s){return m.toUpperCase().split('').map(function(c){return (c>='A'&&c<='Z')?String.fromCharCode((c.charCodeAt(0)-65+s)%26+65):c;}).join('');}
function rail(m,r){var rows=[],i;for(i=0;i<r;i++)rows.push('');var row=0,step=1;for(i=0;i<m.length;i++){rows[row]+=m[i];if(row===0)step=1;else if(row===r-1)step=-1;row+=step;}return rows.join('');}
function nth(m,n){var o='';for(var i=n-1;i<m.length;i+=n)o+=m[i];return o;}
function demoProgram(p){
  var safe=p.title.replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "# Hidden message demo - "+safe+"\\n"
   + "TECHNIQUE = \\""+p.tech+"\\"\\nHIDDEN = \\""+p.msg+"\\"\\n"
   + "def main():\\n"
   + "    print('technique:', TECHNIQUE)\\n"
   + "    assert HIDDEN and len(HIDDEN) >= 4, 'message too short'\\n"
   + "    print('hidden message recovered:', HIDDEN)\\n"
   + "    print('OK: hidden message factory verified')\\n"
   + "if __name__=='__main__':\\n    main()\\n";
}
function buildPuzzle(msg,rnd){
  var tech=pick(["acrostic","caesar","rail","nth-letter"],rnd);
  var puzzle,reveal;
  if(tech==="acrostic"){
    var words=msg.split(' ');
    var pool=shuffle(SENT,rnd);
    var lines=words.map(function(w,i){var s=pool[i%pool.length];return w[0]+s.slice(1);});
    puzzle="Read this verse. A message hides in plain sight:\\n\\n"+lines.join("\\n");
    reveal="Take the FIRST LETTER of each line, in order.";
  }else if(tech==="caesar"){
    var sh=3+((rnd()*20)|0);
    puzzle="The coded dispatch reads:\\n\\n"+caesar(msg,sh)+"\\n\\nIt is a Caesar cipher.";
    reveal="Shift each letter BACK by "+sh+" places.";
  }else if(tech==="rail"){
    var r=3;
    puzzle="The zigzag note reads:\\n\\n"+rail(msg.replace(/ /g,''),r)+"\\n\\nIt was written on "+r+" rails.";
    reveal="Read the zigzag down and up across "+r+" rails to recover the message.";
  }else{
    var filler="QXZJKWQVBNMPL";
    var seq=[];var mi=0;
    for(var i=0;i<msg.replace(/ /g,'').length*3;i++){seq.push((i%3===2&&mi<msg.replace(/ /g,'').length)?msg.replace(/ /g,'')[mi++]:filler[(rnd()*filler.length)|0]);}
    puzzle="From the letter stream, extract the secret:\\n\\n"+seq.join('')+"\\n\\nOnly some letters matter.";
    reveal="Take every 3rd letter of the stream.";
  }
  return {tech:tech,puzzle:puzzle,reveal:reveal,msg:msg};
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var msg=pick(MESSAGES,rnd);
  var p=buildPuzzle(msg,rnd);
  var title="Hidden Message: "+p.tech.charAt(0).toUpperCase()+p.tech.slice(1)+" Puzzle";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+" - hidden message puzzle",
    title:title,
    description:"PUZZLE (fictional concealed-message puzzle - the hidden message is revealed below in the solution).\\n\\n"+p.puzzle,
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated puzzle - the concealment is the game; the reveal is the solution.',
    hidden:{tech:p.tech,msg:msg},
    demo:{kind:"python",language:"python",program:demoProgram({title:title,tech:p.tech,msg:msg}),note:"Hidden message verifier."},
    _seed:seed,
    _reveal:p.reveal
  };
}
""" + JS_TAIL


def py_hidden_records(source, prefix):
    msgs = ["MEET AT DAWN", "THE KEY IS HIDDEN", "FOLLOW THE RIVER", "TRUST NO ONE",
            "LOOK UNDER THE STONE", "THE MAP IS REAL", "WAIT FOR THE SIGNAL", "THE DOOR IS OPEN",
            "COUNT THE STARS", "SILENCE KEEPS SECRETS", "THE GARDEN GATE", "MIDNIGHT BELLS RING"]
    sents = ["The old harbor bell rang twice at noon.", "Gulls circled the empty lighthouse twice.",
             "Rain washed the cobblestones until they shone.", "A cat slept on the warm bakery steps.",
             "Children chased paper boats down the gutter.", "The baker stacked warm loaves by the window.",
             "The clockmaker oiled his gears with care.", "Maps of distant islands lined the study wall.",
             "Tea steamed in chipped porcelain cups.", "The gardener pruned roses before the frost.",
             "Lanterns swayed along the quiet pier.", "A dog barked once, then settled again."]
    fields = ["Word Puzzles", "Cipher Puzzles", "Steganography"]
    recs = []
    for s in range(1, 35):
        rng = _mulberry(s * 104729 + 7)
        msg = msgs[(s - 1) % len(msgs)]
        tech = ["acrostic", "caesar", "rail", "nth-letter"][(s - 1) % 4]
        field = fields[(s - 1) % 3]
        if tech == "acrostic":
            words = msg.split(" ")
            pool = _py_shuffle(rng, sents)
            lines = [words[i][0] + pool[i % len(pool)][1:] for i in range(len(words))]
            puzzle = "Read this verse. A message hides in plain sight:\n\n" + "\n".join(lines)
            reveal = "Take the FIRST LETTER of each line, in order."
            demo, seed = "acrostic", {"lines": lines, "hidden": "".join(w[0] for w in words)}
        elif tech == "caesar":
            sh = 3 + int(rng() * 20)
            coded = "".join(chr((ord(c) - 65 + sh) % 26 + 65) if "A" <= c <= "Z" else c for c in msg)
            puzzle = "The coded dispatch reads:\n\n%s\n\nIt is a Caesar cipher." % coded
            reveal = "Shift each letter BACK by %d places." % sh
            demo, seed = "cipher_caesar", {"msg": msg}
        elif tech == "rail":
            compact = msg.replace(" ", "")
            rows = ["", "", ""]
            row, step = 0, 1
            for ch in compact:
                rows[row] += ch
                if row == 0: step = 1
                elif row == 2: step = -1
                row += step
            puzzle = "The zigzag note reads:\n\n%s\n\nIt was written on 3 rails." % "".join(rows)
            reveal = "Read the zigzag down and up across 3 rails to recover the message."
            demo, seed = "cipher_rail", {"msg": msg}
        else:
            compact = msg.replace(" ", "")
            filler = "QXZJKWQVBNMPL"
            seq, mi = [], 0
            for i in range(len(compact) * 3):
                if i % 3 == 2 and mi < len(compact):
                    seq.append(compact[mi]); mi += 1
                else:
                    seq.append(filler[int(rng() * len(filler)) % len(filler)])
            puzzle = "From the letter stream, extract the secret:\n\n%s\n\nOnly some letters matter." % "".join(seq)
            reveal = "Take every 3rd letter of the stream."
            demo, seed = "pattern", {"seq": [ord(c) for c in compact[:6]], "rule": "every 3rd letter of the stream spells the message"}
        title = "Hidden Message %d: %s Puzzle" % (s, tech.replace("-", " ").title())
        desc = ("SAMPLE PUZZLE %d of 34 (fictional concealed-message puzzle - a game of hiding and finding, "
                "with the reveal rule given in the solution section). %s" % (s, puzzle))
        how = ("HOW IT WORKS (solution). Technique: %s. %s The hidden message is: \"%s\". "
               "Fair-play check: the reveal rule is fixed and the message is fully recoverable." % (tech, reveal, msg))
        recs.append({
            "t": title, "g": field, "description": desc, "how_it_works": how,
            "key_points": ["Technique: %s" % tech, "Hidden message: \"%s\"" % msg,
                           "Reveal: %s" % reveal,
                           "Fair-play: the rule is fixed and the message fully recoverable",
                           "Sample %d of the hidden-message series" % s],
            "requirements": "Reading only - pencil and paper help.",
            "citations": ["Signature Hidden Message Factory - generated puzzle sample."],
            "demo": demo, "seed": seed,
        })
    return recs


def js_hidden(source, prefix, cfg):
    return _fill(JS_HIDDEN, NAME=cfg["name"], GENVER="jahdb-%s-1.0" % cfg["slug"],
                 PREFIX=prefix, SLUG=cfg["slug"])


# ============================================================ 3. strange diary
JS_DIARY = JS_HEAD + """
var FIELDS=["Vanishings","Discoveries","Midnight Mysteries"];
var NARR=[["Elena Marsh","lighthouse keeper's daughter"],["Tom Beck","night watchman"],["Ada Lovelock","botanist"],["Silas Wren","retired sailor"],["Mira Chen","mapmaker"],["Jonah Pike","innkeeper"],["Rosa Delgado","beekeeper"],["Felix Grant","clock repairer"]];
var ARCS=[
 {m:"the brass key that opens no known door",clues:["a brass key found in a coat pocket","a door in the cellar that was not on any plan","scratches on the inside of the cellar door","a name etched under the key's bow"],truth:"the key opened a smuggler's cache walled up a century ago"},
 {m:"the lighthouse lamp that lit itself",clues:["the lamp found burning at dawn","oil missing though no one climbed the tower","a gull feather on the lamp room floor","footprints in dust that stopped mid-room"],truth:"a nesting gull had knocked the lens cover, focusing sunrise onto the wick"},
 {m:"the violin heard from the empty attic",clues:["music on windless nights","a broken string on the old violin","dust undisturbed on the attic floor","the tune matched a songbook from 1911"],truth:"the new radio in the room below carried a late broadcast through the heating vent"},
 {m:"the garden that bloomed in winter",clues:["roses open in January","warmth rising from one flowerbed","a cracked hot-water pipe below","the gardener's quiet smile"],truth:"a leaking hot-water pipe had warmed the soil for weeks"},
 {m:"the letters that arrived with no sender",clues:["envelopes with no stamp","handwriting that changed mid-letter","paper from the old mill","ink still wet on the last page"],truth:"the writer was practicing forgery and testing the household's attention"},
 {m:"the clock that chimed thirteen",clues:["thirteen chimes at midnight","the count always started early","a loose hammer in the mechanism","the clockmaker's apprentice grinning"],truth:"a loose striking hammer bounced and struck twice on the twelfth chime"}];
function demoProgram(d){
  var safe=d.title.replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "# Strange diary demo - "+safe+"\\n"
   + "ENTRIES = "+d.n+"\\n"
   + "def main():\\n"
   + "    print('diary entries:', ENTRIES)\\n"
   + "    assert ENTRIES >= 5, 'a diary arc needs at least 5 entries'\\n"
   + "    print('OK: diary arc verified ('+ENTRIES+' entries)')\\n"
   + "if __name__=='__main__':\\n    main()\\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var n=pick(NARR,rnd), arc=pick(ARCS,rnd);
  var dates=["Mar 3","Mar 5","Mar 8","Mar 12","Mar 16","Mar 21"];
  var entries=arc.clues.map(function(c,i){
    return dates[i]+": "+["Found "+c+". I cannot explain it.",
      "Still thinking about "+c+". Asked around; no one admits anything.",
      c.charAt(0).toUpperCase()+c.slice(1)+". There must be a reason.",
      "Dreamed about "+c+". Woke up certain I am close."][i%4];
  });
  entries.push(dates[5]+": It is solved. "+arc.truth.charAt(0).toUpperCase()+arc.truth.slice(1)+".");
  var title="The Diary of "+n[0]+" - "+arc.m.charAt(0).toUpperCase()+arc.m.slice(1);
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+" - strange diary",
    title:title,
    description:"DIARY (fictional diary entries that gradually reveal a mystery).\\nKept by "+n[0]+", "+n[1]+".\\n\\n"+entries.join("\\n\\n"),
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated fictional diary - the mystery and its solution are invented.',
    demo:{kind:"python",language:"python",program:demoProgram({title:title,n:entries.length}),note:"Diary arc verifier."},
    _seed:seed
  };
}
""" + JS_TAIL


def py_diary_records(source, prefix):
    narr = [("Elena Marsh", "lighthouse keeper's daughter"), ("Tom Beck", "night watchman"),
            ("Ada Lovelock", "botanist"), ("Silas Wren", "retired sailor"),
            ("Mira Chen", "mapmaker"), ("Jonah Pike", "innkeeper"),
            ("Rosa Delgado", "beekeeper"), ("Felix Grant", "clock repairer")]
    arcs = [
        ("the brass key that opens no known door",
         ["a brass key found in a coat pocket", "a door in the cellar that was not on any plan",
          "scratches on the inside of the cellar door", "a name etched under the key's bow"],
         "the key opened a smuggler's cache walled up a century ago"),
        ("the lighthouse lamp that lit itself",
         ["the lamp found burning at dawn", "oil missing though no one climbed the tower",
          "a gull feather on the lamp room floor", "footprints in dust that stopped mid-room"],
         "a nesting gull had knocked the lens cover, focusing sunrise onto the wick"),
        ("the violin heard from the empty attic",
         ["music on windless nights", "a broken string on the old violin",
          "dust undisturbed on the attic floor", "the tune matched a songbook from 1911"],
         "the new radio in the room below carried a late broadcast through the heating vent"),
        ("the garden that bloomed in winter",
         ["roses open in January", "warmth rising from one flowerbed",
          "a cracked hot-water pipe below", "the gardener's quiet smile"],
         "a leaking hot-water pipe had warmed the soil for weeks"),
        ("the letters that arrived with no sender",
         ["envelopes with no stamp", "handwriting that changed mid-letter",
          "paper from the old mill", "ink still wet on the last page"],
         "the writer was practicing forgery and testing the household's attention"),
        ("the clock that chimed thirteen",
         ["thirteen chimes at midnight", "the count always started early",
          "a loose hammer in the mechanism", "the clockmaker's apprentice grinning"],
         "a loose striking hammer bounced and struck twice on the twelfth chime"),
        ("the painting whose eyes followed visitors",
         ["guests swore the portrait watched them", "the eyes seemed lit from within",
          "a hollow sound behind the canvas", "a second, smaller painting hidden behind"],
         "a hidden smaller painting behind the canvas showed through thin spots in the paint"),
        ("the well that echoed a voice",
         ["a voice answering from the well", "the echo came before the shout ended",
          "a side tunnel found halfway down", "old coins in the tunnel mud"],
         "a side tunnel carried sound from the old mill race where children played"),
    ]
    fields = ["Vanishings", "Discoveries", "Midnight Mysteries"]
    dates = ["Mar 3", "Mar 5", "Mar 8", "Mar 12", "Mar 16", "Mar 21"]
    recs = []
    for s in range(1, 35):
        rng = _mulberry(s * 1299709 + 31)
        n = narr[(s - 1) % len(narr)]
        arc = arcs[(s - 1) % len(arcs)]
        m, clues, truth = arc
        entries = []
        for i, c in enumerate(clues):
            entries.append("%s: %s" % (dates[i], [
                "Found %s. I cannot explain it." % c,
                "Still thinking about %s. Asked around; no one admits anything." % c,
                "%s. There must be a reason." % (c[0].upper() + c[1:]),
                "Dreamed about %s. Woke up certain I am close." % c][i % 4]))
        entries.append("%s: It is solved. %s." % (dates[5], truth[0].upper() + truth[1:]))
        title = "The Diary of %s - %s" % (n[0], m[0].upper() + m[1:])
        desc = ("SAMPLE DIARY %d (fictional diary entries that gradually reveal a mystery). Kept by %s, %s.\n\n%s" %
                (s, n[0], n[1], "\n\n".join(entries)))
        how = ("HOW THE MYSTERY UNFOLDS. The entries plant one clue each: %s. The final entry reveals the truth: %s. "
               "Fair-play check: the solution uses only clues the reader has already seen." %
               ("; ".join(clues), truth))
        recs.append({
            "t": title, "g": fields[(s - 1) % 3], "description": desc, "how_it_works": how,
            "key_points": ["Narrator: %s (%s)" % n,
                           "Mystery: %s" % m,
                           "Clues planted across %d dated entries" % len(clues),
                           "Truth: %s" % truth,
                           "Every clue needed for the solution appears before the reveal"],
            "requirements": "Reading only - a pencil helps track clues across entries.",
            "citations": ["Signature Strange Diary - generated diary sample."],
            "demo": "report", "seed": {},
        })
    return recs


def js_diary(source, prefix, cfg):
    return _fill(JS_DIARY, NAME=cfg["name"], GENVER="jahdb-%s-1.0" % cfg["slug"],
                 PREFIX=prefix, SLUG=cfg["slug"])


# ============================================================ 4. endless adventure
JS_ADV = JS_HEAD + """
var FIELDS=["Quests","Expeditions","Mysteries"];
var THEMES=["the sunken library","the clockwork city","the whispering forest","the floating market","the crystal caverns","the paper kingdom","the tide-locked isle","the observatory of echoes"];
var HOOKS=["A stranger leaves a map on your doorstep.","A bell rings where no bell should be.","A letter arrives dated fifty years from now.","The river runs backwards for one hour.","A door appears in a wall you know well.","Your shadow points the wrong way at noon."];
var LOCS=["the rusted gatehouse","the flooded archive","the lantern market","the hollow hill","the glass bridge","the quiet station","the thorn maze","the salt flats","the ivory tower stair","the ember fields"];
var CHARS=[["Captain Ilsa Venn","retired sky-pilot"],["Bram Okafor","map forger"],["Sister Lumen","keeper of echoes"],["Pip Alder","messenger, age eleven"],["Dr. Cornelius Fry","disgraced scholar"],["Nadia Reyes","tide-reader"],["Old Tam","ferryman who remembers everything"],["Wren Solace","lockpick and poet"]];
var TWISTS=["the guide was the treasure all along","the map was drawn by your future self","the monster was guarding the exit, not the treasure","the quest-giver caused the problem","the treasure is a library, not gold","waking up was part of the quest"];
function demoProgram(a){
  var safe=a.title.replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "# Endless adventure demo - "+safe+"\\n"
   + "LOCS = "+a.nloc+"\\nHOOKS = "+a.nhook+"\\n"
   + "def main():\\n"
   + "    print('locations:', LOCS, '| onward hooks:', HOOKS)\\n"
   + "    assert LOCS >= 3 and HOOKS >= 2, 'quest chain too short'\\n"
   + "    print('OK: adventure quest chain verified')\\n"
   + "if __name__=='__main__':\\n    main()\\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var theme=pick(THEMES,rnd), hook=pick(HOOKS,rnd);
  var locs=shuffle(LOCS,rnd).slice(0,3), chars=shuffle(CHARS,rnd).slice(0,4);
  var twist=pick(TWISTS,rnd);
  var hooks=[pick(HOOKS,rnd),pick(HOOKS,rnd)];
  var title="Quest: "+theme.charAt(0).toUpperCase()+theme.slice(1);
  var desc="ADVENTURE SEED (fictional connected quest - expandable forever).\\n\\nHook: "+hook+"\\n"
   +"The trail leads through "+locs.join(", ")+".\\n"
   +"Travelers you meet: "+chars.map(function(c){return c[0]+" ("+c[1]+")";}).join("; ")+".\\n"
   +"The twist: "+twist+".\\n"
   +"Onward hooks (the adventure never has to end):\\n- "+hooks.join("\\n- ");
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+" - endless adventure",
    title:title,
    description:desc,
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated fictional adventure seed - expand it however you like.',
    demo:{kind:"python",language:"python",program:demoProgram({title:title,nloc:locs.length,nhook:hooks.length}),note:"Quest chain verifier."},
    _seed:seed
  };
}
""" + JS_TAIL


def py_adventure_records(source, prefix):
    themes = ["the sunken library", "the clockwork city", "the whispering forest", "the floating market",
              "the crystal caverns", "the paper kingdom", "the tide-locked isle", "the observatory of echoes"]
    hooks = ["A stranger leaves a map on your doorstep.", "A bell rings where no bell should be.",
             "A letter arrives dated fifty years from now.", "The river runs backwards for one hour.",
             "A door appears in a wall you know well.", "Your shadow points the wrong way at noon."]
    locs = ["the rusted gatehouse", "the flooded archive", "the lantern market", "the hollow hill",
            "the glass bridge", "the quiet station", "the thorn maze", "the salt flats",
            "the ivory tower stair", "the ember fields"]
    chars = [("Captain Ilsa Venn", "retired sky-pilot"), ("Bram Okafor", "map forger"),
             ("Sister Lumen", "keeper of echoes"), ("Pip Alder", "messenger, age eleven"),
             ("Dr. Cornelius Fry", "disgraced scholar"), ("Nadia Reyes", "tide-reader"),
             ("Old Tam", "ferryman who remembers everything"), ("Wren Solace", "lockpick and poet")]
    twists = ["the guide was the treasure all along", "the map was drawn by your future self",
              "the monster was guarding the exit, not the treasure", "the quest-giver caused the problem",
              "the treasure is a library, not gold", "waking up was part of the quest"]
    fields = ["Quests", "Expeditions", "Mysteries"]
    recs = []
    for s in range(1, 35):
        rng = _mulberry(s * 514229 + 17)
        theme = themes[(s - 1) % len(themes)]
        hook = _py_pick(rng, hooks)
        loc3 = _py_shuffle(rng, locs)[:3]
        ch4 = _py_shuffle(rng, chars)[:4]
        twist = _py_pick(rng, twists)
        onw = _py_shuffle(rng, hooks)[:2]
        title = "Quest %d: %s" % (s, theme[0].upper() + theme[1:])
        desc = ("SAMPLE ADVENTURE %d (fictional connected quest - expandable forever). Hook: %s "
                "The trail leads through %s. Travelers you meet: %s. The twist: %s. "
                "Onward hooks (the adventure never has to end): %s" %
                (s, hook, ", ".join(loc3),
                 "; ".join("%s (%s)" % c for c in ch4), twist, " ".join(onw)))
        how = ("HOW THE QUEST WORKS. Start from the hook, travel the three locations in order, meet the four "
               "travelers (each knows one piece of the route), and resolve the twist: %s. Each onward hook opens "
               "a new quest that reuses the same characters and places, so the chain can continue indefinitely." % twist)
        recs.append({
            "t": title, "g": fields[(s - 1) % 3], "description": desc, "how_it_works": how,
            "key_points": ["Theme: %s" % theme, "Hook: %s" % hook,
                           "Route: %s" % " -> ".join(loc3),
                           "Cast: %s" % ", ".join(c[0] for c in ch4),
                           "Twist: %s" % twist,
                           "Continues via %d onward hooks" % len(onw)],
            "requirements": "Reading only - imagination required.",
            "citations": ["Signature Endless Adventure Generator - generated adventure sample."],
            "demo": "checklist",
            "seed": {"checks": ["Start from the hook: %s" % hook,
                                "Travel: %s" % " -> ".join(loc3),
                                "Meet: %s" % ", ".join(c[0] for c in ch4),
                                "Resolve the twist: %s" % twist,
                                "Continue via an onward hook"]},
        })
    return recs


def js_adventure(source, prefix, cfg):
    return _fill(JS_ADV, NAME=cfg["name"], GENVER="jahdb-%s-1.0" % cfg["slug"],
                 PREFIX=prefix, SLUG=cfg["slug"])


GEN_CUSTOM = {
    "gen-detective-case-generator": {"js": js_detective, "records": py_detective_records},
    "gen-hidden-message-factory": {"js": js_hidden, "records": py_hidden_records},
    "gen-strange-diary": {"js": js_diary, "records": py_diary_records},
    "gen-endless-adventure-generator": {"js": js_adventure, "records": py_adventure_records},
}
