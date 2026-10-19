#!/usr/bin/env python3
"""REAL working client-side generators for the 7 GENERATOR-class items.

Each rendered gen-<slug>.js produces genuine outputs (verified palindromes,
full celebration messages, full thank-you notes, real quiz rounds, real
deeds, real friendship sessions, real social adventures) — never structural
samples. Deterministic: same seed, same output.

Property of Justin Addam Higgins (JAH).
"""
import json
import os
import subprocess
import sys

REPO = os.path.expanduser("~/workspace/jah-databases")


def _js_str(s):
    return json.dumps(s, ensure_ascii=False)


HEADER = """(function(){'use strict';
/* JAH @@NAME@@ — REAL generator — @@GENVER@@.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same output. Every run produces a genuine,
   fully-formed new item — never a structural sample. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,s){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(s()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
function fill(t,slots,s){var out=t;Object.keys(slots).forEach(function(k){out=out.split('{'+k+'}').join(pick(slots[k],s));});return out;}
function pyDemo(title,text){
  var t=String(text).replace(/\\\\/g,'\\\\\\\\').replace(/\"\"\"/g,'\\\\\"\\\\\"\\\\\"');
  var h=String(title).replace(/[\\r\\n]+/g,' ').slice(0,120);
  return '# '+h+'\\n# Property of Justin Addam Higgins (JAH).\\n'
    + 'ITEM = \"\"\"'+t+'\"\"\"\\n'
    + 'print(ITEM)\\n'
    + 'assert len(ITEM) > 40, "empty generated item"\\n'
    + 'assert "{" not in ITEM, "unfilled slot in generated item"\\n'
    + 'print("generated_chars=%d" % len(ITEM))\\n'
    + 'print("DEMO OK")\\n';
}
var PREFIX=@@PREFIX@@;
var SRC=@@SRC@@;
var RECORD_KIND=@@RECORD_KIND@@;
"""

FOOTER = """
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\\\-')+'\\\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.description||r.description.length<40)e.push('description');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:@@GENVER@@,generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(@@SLUG@@,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""

# ------------------------------------------------------------------ palindromes
PAL_BODY = """
var FIELDS=["Word Palindromes","Phrase Palindromes","Palindrome Builder","Name Palindromes"];
var WORDS=@@WORDS@@;
var PHRASES=@@PHRASES@@;
var NAMES=@@NAMES@@;
var BUILD_A=["step","live","star","draw","loop","part","straw","diaper","reward","dennis"];
var BUILD_B=["on","it","up","at","in","so"];
function letters(s){return s.toLowerCase().replace(/[^a-z]/g,'');}
function isPal(s){var l=letters(s);return l===l.split('').reverse().join('')&&l.length>2;}
function rev(w){return w.split('').reverse().join('');}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var title,body,proof;
  if(field==="Word Palindromes"){
    var w=pick(WORDS,rnd);
    if(!isPal(w))throw new Error('pool word failed palindrome check: '+w);
    title='Palindrome word: "'+w+'"';
    proof='Letters "'+letters(w)+'" reversed are "'+letters(w).split('').reverse().join('')+'" — identical.';
    body='The word "'+w+'" reads the same forward and backward. '+proof+' It has '+w.length+' letters. Say it aloud forward, then backward: it never changes. Word palindromes like this one are the building blocks of the playground — collect them, then combine them into phrases.';
  }else if(field==="Phrase Palindromes"){
    var p=pick(PHRASES,rnd);
    if(!isPal(p))throw new Error('pool phrase failed palindrome check: '+p);
    title='Palindrome phrase: "'+p+'"';
    proof='Stripped to letters, "'+letters(p)+'" reversed is identical — a true phrase palindrome.';
    body='"'+p+'" is a genuine phrase palindrome. '+proof+' ('+letters(p).length+' letters.) Phrase palindromes ignore spaces, punctuation, and capitalization; only the letter order matters. Try writing it backward yourself to feel the symmetry.';
  }else if(field==="Name Palindromes"){
    var n=pick(NAMES,rnd);
    if(!isPal(n))throw new Error('pool name failed palindrome check: '+n);
    title='Palindrome name: "'+n+'"';
    proof='Letters "'+letters(n)+'" reversed are identical.';
    body='"'+n+'" is a palindrome name. '+proof+' Palindrome names are favorites for characters, pets, and pen names — the same forward and backward, like the person wearing it two ways at once.';
  }else{
    var a=pick(BUILD_A,rnd),b=pick(BUILD_B,rnd);
    var phrase=a+' '+b+' '+rev(b)+' '+rev(a);
    if(!isPal(phrase))throw new Error('builder produced non-palindrome: '+phrase);
    title='Built palindrome: "'+phrase+'"';
    proof='Construction: "'+a+'" + "'+b+'" + reverse("'+b+'")="'+rev(b)+'" + reverse("'+a+'")="'+rev(a)+'". Letters "'+letters(phrase)+'" reversed are identical — guaranteed by the mirror construction.';
    body='Fresh-built palindrome: "'+phrase+'". '+proof+' The Palindrome Builder mirrors any two words around a center: A + B + reverse(B) + reverse(A) always reads the same backward. ('+letters(phrase).length+' letters.) Swap in your own words and the mirror still holds — that is the whole trick, and now it is yours.';
  }
  var desc='NEW PALINDROME (generated). '+body;
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — '+RECORD_KIND,
    title:title,
    description:desc,
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated palindrome — machine-verified to read the same backward. Seeded archive records are the authoritative entries.',
    demo:{kind:'palindrome-verified',language:'python',program:pyDemo(title,desc),note:'Verified palindrome; demo prints the generated item.'},
    _seed:seed
  };
}
"""

# ------------------------------------------------------------------ good deeds
DEED_BODY = """
var FIELDS=["Quick Deeds","Planned Deeds","Big-Hearted Deeds"];
var DEEDS=@@DEEDS@@;
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=DEEDS[field];
  var d=pick(pool,rnd);
  var text=fill(d.text,d.slots,rnd);
  var steps=d.steps.map(function(s,i){return (i+1)+'. '+fill(s,d.slots,rnd);});
  var title='Good deed: '+d.name;
  var body='YOUR GOOD DEED — '+d.name.toUpperCase()+'\\n\\n'+text+'\\n\\nHow to do it:\\n'+steps.join('\\n')
    +'\\n\\nTime needed: '+d.time+'. Cost: '+d.cost+'. '
    +'Do it today if you can — small kindnesses compound. When it is done, notice how it felt; that feeling is the real reward, and it is why this generator exists.';
  var desc='NEW GOOD DEED (generated). '+body;
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — '+RECORD_KIND,
    title:title,
    description:desc,
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated good-deed plan. Seeded archive records are the authoritative entries.',
    demo:{kind:'good-deed-plan',language:'python',program:pyDemo(title,desc),note:'Demo prints the generated deed plan.'},
    _seed:seed
  };
}
"""

# ------------------------------------------------------------------ celebration messages
CELEB_BODY = """
var FIELDS=@@OCCASIONS@@;
var RELS=["friend","sister","brother","mom","dad","partner","coworker","neighbor","grandparent","child","cousin","mentor"];
var NAMES=["Alex","Jordan","Taylor","Sam","Riley","Casey","Jamie","Morgan","Avery","Quinn","Drew","Robin"];
var TPL=@@TPL@@;
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var tpls=TPL[field];
  var t=pick(tpls,rnd);
  var msg=fill(t,{name:pick(NAMES,rnd),rel:pick(RELS,rnd)},rnd);
  var title=field+' message for '+msg.split(' ')[0].replace(/[^A-Za-z]/g,'');
  var body='YOUR CELEBRATION MESSAGE — '+field.toUpperCase()+'\\n\\n'+msg+'\\n\\nCopy it as-is, or swap in the real name and one personal detail (an inside joke, a shared memory) to make it unmistakably yours. Handwritten beats typed; spoken beats texted.';
  var desc='NEW CELEBRATION MESSAGE (generated). '+body;
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — '+RECORD_KIND,
    title:title,
    description:desc,
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated message — personalize with a real name and detail before sending. Seeded archive records are the authoritative entries.',
    demo:{kind:'celebration-message',language:'python',program:pyDemo(title,desc),note:'Demo prints the generated message.'},
    _seed:seed
  };
}
"""

# ------------------------------------------------------------------ thank-you notes
THANK_BODY = """
var FIELDS=["For a Gift","For Help","For Hospitality","For Kind Words","For an Opportunity"];
var NAMES=["Alex","Jordan","Taylor","Sam","Riley","Casey","Jamie","Morgan","Avery","Quinn"];
var TPL=@@TPL@@;
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var tpls=TPL[field];
  var t=pick(tpls,rnd);
  var note=fill(t,{name:pick(NAMES,rnd)},rnd);
  var title='Thank-you note ('+field.toLowerCase()+')';
  var body='YOUR THANK-YOU NOTE\\n\\n'+note+'\\n\\nThe anatomy of a note that lands: name the thing, name the feeling, name the future. Replace the sample name with the real one, add one specific detail only you would know, and send it within a week — late gratitude still counts.';
  var desc='NEW THANK-YOU NOTE (generated). '+body;
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — '+RECORD_KIND,
    title:title,
    description:desc,
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated note — personalize before sending. Seeded archive records are the authoritative entries.',
    demo:{kind:'thank-you-note',language:'python',program:pyDemo(title,desc),note:'Demo prints the generated note.'},
    _seed:seed
  };
}
"""

# ------------------------------------------------------------------ friendship builder
FRIEND_BODY = """
var FIELDS=["Friendship Activities","Conversation Decks","Kindness Challenges"];
var ACTIVITIES=@@ACTIVITIES@@;
var QUESTIONS=@@QUESTIONS@@;
var CHALLENGES=@@CHALLENGES@@;
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var title,body;
  if(field==="Friendship Activities"){
    var a=pick(ACTIVITIES,rnd);
    var steps=a.steps.map(function(s,i){return (i+1)+'. '+s;});
    title='Friendship activity: '+a.name;
    body='YOUR FRIENDSHIP SESSION\\n\\nActivity: '+a.name+'\\n'+a.desc+'\\n\\nPlan:\\n'+steps.join('\\n')
      +'\\n\\nYou will need: '+a.materials+'. Time: '+a.time+'. Best with '+a.group+'. '
      +'Then open the conversation deck below — three cards, everyone answers.\\n\\nConversation cards:\\n'
      +shuffle(QUESTIONS,rnd).slice(0,3).map(function(q,i){return 'Card '+(i+1)+': '+q;}).join('\\n');
  }else if(field==="Conversation Decks"){
    var cards=shuffle(QUESTIONS,rnd).slice(0,5);
    title='Conversation deck ('+cards.length+' cards)';
    body='YOUR CONVERSATION DECK — deal one card at a time, everyone answers before moving on.\\n\\n'
      +cards.map(function(q,i){return 'Card '+(i+1)+': '+q;}).join('\\n')
      +'\\n\\nHouse rule: no deflecting with "what about you?" until you have answered yourself. The deck works because the questions do the asking for you.';
  }else{
    var c=pick(CHALLENGES,rnd);
    var steps=c.steps.map(function(s,i){return (i+1)+'. '+s;});
    title='Kindness challenge: '+c.name;
    body='YOUR KINDNESS CHALLENGE — '+c.name.toUpperCase()+'\\n\\n'+c.desc+'\\n\\nSteps:\\n'+steps.join('\\n')
      +'\\n\\nComplete it within '+c.window+'. Tell one person you did it — not to brag, but because kindness told is kindness multiplied.';
  }
  var desc='NEW FRIENDSHIP BUILDER SESSION (generated). '+body;
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — '+RECORD_KIND,
    title:title,
    description:desc,
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated friendship session. Seeded archive records are the authoritative entries.',
    demo:{kind:'friendship-session',language:'python',program:pyDemo(title,desc),note:'Demo prints the generated session.'},
    _seed:seed
  };
}
"""

# ------------------------------------------------------------------ family games
FAMILY_BODY = """
var FIELDS=["Quiz Round","Scavenger Hunt","Charades Deck","Story Builder"];
var QUIZ=@@QUIZ@@;
var HUNT=@@HUNT@@;
var CHARADES=@@CHARADES@@;
var STARTERS=@@STARTERS@@;
var TWISTS=@@TWISTS@@;
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var title,body;
  if(field==="Quiz Round"){
    var qs=shuffle(QUIZ,rnd).slice(0,5);
    title='Family quiz round ('+qs.length+' questions)';
    body='FAMILY QUIZ ROUND — read each question aloud; players write answers secretly. Answers are at the bottom, no peeking.\\n\\n'
      +qs.map(function(q,i){return 'Q'+(i+1)+': '+q.q;}).join('\\n')
      +'\\n\\nScoring: 1 point per correct answer, bonus point for the funniest wrong answer (family vote).\\n\\nANSWERS (no peeking):\\n'
      +qs.map(function(q,i){return 'A'+(i+1)+': '+q.a;}).join('\\n');
  }else if(field==="Scavenger Hunt"){
    var items=shuffle(HUNT,rnd).slice(0,8);
    title='Family scavenger hunt ('+items.length+' items)';
    body='FAMILY SCAVENGER HUNT — 20 minutes on the clock. Find each item and bring it (or photograph it) back to base.\\n\\n'
      +items.map(function(it,i){return (i+1)+'. '+it;}).join('\\n')
      +'\\n\\nScoring: 1 point per item, 2 points if the whole family agrees it was the most creative find. Grown-ups play too — no sidelines in this family.';
  }else if(field==="Charades Deck"){
    var cards=shuffle(CHARADES,rnd).slice(0,8);
    title='Family charades deck ('+cards.length+' cards)';
    body='FAMILY CHARADES — no talking, no pointing at objects, sounds and gestures only. 60 seconds per card.\\n\\n'
      +cards.map(function(c,i){return 'Card '+(i+1)+' ['+c.d+']: '+c.w;}).join('\\n')
      +'\\n\\nLittle kids get the Easy cards first; let them deal. The actor may not speak — the guessers may shout all they want.';
  }else{
    var st=pick(STARTERS,rnd);
    var tw=shuffle(TWISTS,rnd).slice(0,3);
    title='Family story builder';
    body='FAMILY STORY BUILDER — one person reads the starter, then players take turns adding one sentence each. When a twist card appears, the next player MUST work it in.\\n\\nStarter: '+st
      +'\\n\\nTwist cards (in order):\\n'+tw.map(function(t,i){return (i+1)+'. '+t;}).join('\\n')
      +'\\n\\nKeep going until someone says "the end" and everyone agrees. Write down the best lines — family lore starts here.';
  }
  var desc='NEW FAMILY GAME (generated). '+body;
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — '+RECORD_KIND,
    title:title,
    description:desc,
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated family game — answers included where needed. Seeded archive records are the authoritative entries.',
    demo:{kind:'family-game',language:'python',program:pyDemo(title,desc),note:'Demo prints the generated game.'},
    _seed:seed
  };
}
"""

# ------------------------------------------------------------------ social adventures
ADV_BODY = """
var FIELDS=["Day Adventures","Evening Adventures","Weekend Adventures"];
var ADV=@@ADV@@;
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var a=pick(ADV[field],rnd);
  var roles=a.roles.map(function(r,i){return ' - '+r;});
  var checks=a.checklist.map(function(c,i){return (i+1)+'. [ ] '+c;});
  var title='Social adventure: '+a.name;
  var body='YOUR SOCIAL ADVENTURE — '+a.name.toUpperCase()+'\\n\\nThe mission: '+a.mission+'\\n\\nWhere: '+a.venue+'\\nCrew: '+a.crew
    +'\\n\\nAssign roles (everyone gets one):\\n'+roles.join('\\n')
    +'\\n\\nAdventure checklist:\\n'+checks.join('\\n')
    +'\\n\\nDebrief (ask these on the way home):\\n'+a.debrief.map(function(d,i){return (i+1)+'. '+d;}).join('\\n')
    +'\\n\\nRule zero: nobody gets left out, nobody gets teased for trying. Adventures are measured in stories told afterward.';
  var desc='NEW SOCIAL ADVENTURE (generated). '+body;
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — '+RECORD_KIND,
    title:title,
    description:desc,
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated adventure plan — check venues and weather before heading out. Seeded archive records are the authoritative entries.',
    demo:{kind:'social-adventure',language:'python',program:pyDemo(title,desc),note:'Demo prints the generated adventure.'},
    _seed:seed
  };
}
"""

POOLS = {}


def _pal_pools():
    words = ["racecar","level","rotor","civic","kayak","madam","refer","rotator","deified",
             "repaper","reviver","stats","solos","tenet","radar","minim","redder","noon",
             "peep","wow","anna","otto","hannah","redivider","detartrated","malayalam",
             "aibohphobia","tattarrattat"]
    phrases = ["A man, a plan, a canal: Panama",
               "Was it a car or a cat I saw",
               "Never odd or even",
               "Do geese see God",
               "Madam, in Eden, I'm Adam",
               "Able was I ere I saw Elba",
               "Go hang a salami, I'm a lasagna hog",
               "A Toyota's a Toyota",
               "Borrow or rob",
               "Don't nod",
               "Live on time, emit no evil",
               "Mr. Owl ate my metal worm",
               "No lemon, no melon",
               "Pull up if I pull up",
               "Rise to vote, sir",
               "Step on no pets",
               "Taco cat",
               "Too bad I hid a boot",
               "Was it a bat I saw",
               "Yo, banana boy",
               "Some men interpret nine memos",
               "Evil is a name of a foeman, as I live"]
    names = ["Anna","Otto","Hannah","Bob","Ava","Eve","Ada","Asa","Elle","Ewe","Halah",
             "Renner","Nayan","Navan","Sahas"]
    # verify every pool entry is a real palindrome (letters only)
    def letters(s):
        return "".join(c for c in s.lower() if c.isalpha())
    for lst, nm in ((words, "words"), (phrases, "phrases"), (names, "names")):
        for w in lst:
            l = letters(w)
            assert l == l[::-1] and len(l) > 2, "not a palindrome: %r" % w
    return {"WORDS": words, "PHRASES": phrases, "NAMES": names}


def _deed_pools():
    def D(name, text, slots, steps, time, cost):
        return {"name": name, "text": text, "slots": slots, "steps": steps,
                "time": time, "cost": cost}
    who = ["a coworker who looks tired", "an elderly neighbor", "a new student at school",
           "a busy parent at the park", "a cashier having a long day", "a friend you have not called in months",
           "a teacher", "a nurse", "a bus driver", "a librarian"]
    where = ["on their desk", "in their mailbox", "taped to their locker", "on the break-room table",
             "inside a library book", "on their windshield (kindly!)"]
    quick = [
        D("The Two-Minute Note",
          "Write a two-minute thank-you note to {who} and leave it {where}.",
          {"who": who, "where": where},
          ["Grab any paper and pen — fancy is optional.",
           "Write one specific thing you appreciate about {who}.",
           "Sign it, leave it {where}, and walk away smiling."],
          "2 minutes", "free"),
        D("Compliment Relay",
          "Give {who} a genuine, specific compliment today, then ask them to pass one on.",
          {"who": who},
          ["Notice one real thing {who} does well.",
           "Say it plainly: 'I noticed X, and it matters.'",
           "Ask them to compliment someone else before sundown."],
          "3 minutes", "free"),
        D("Cart Return Hero",
          "Return three stray shopping carts to the corral on your next store trip — including ones that are not yours.",
          {"who": ["a stranger", "the next shopper"]},
          ["Spot stray carts in the lot.",
           "Wheel each one to the corral (three is the goal).",
           "Enjoy the tiny workout and the clear conscience."],
          "5 minutes", "free"),
        D("Water-Bottle Refill",
          "Refill the shared water pitcher or the pet bowls at {where}.",
          {"where": ["the office kitchen", "the park fountain area", "home"]},
          ["Check the shared water source near you.",
           "Clean and refill it fully.",
           "Tell no one. Let someone just find it full."],
          "4 minutes", "free"),
    ]
    planned = [
        D("The Neighbor Check-In",
          "Visit {who} this week with {gift} and stay for a real conversation.",
          {"who": ["an elderly neighbor", "a new neighbor", "a neighbor living alone"],
           "gift": ["baked cookies", "extra soup", "a small plant", "a handwritten card"]},
          ["Pick a day and a {gift} to bring.",
           "Knock, introduce (or reintroduce) yourself warmly.",
           "Ask one real question and actually listen to the answer.",
           "Offer one specific help: 'I can carry groceries Tuesdays.'"],
          "30 minutes", "a few dollars"),
        D("Little Library Restock",
          "Restock a little free library (or start a give-one box) near {where}.",
          {"where": ["your street", "the park", "school", "the community center"]},
          ["Gather 5-10 books you have finished.",
           "Find the nearest little library or a visible shelf spot.",
           "Shelve them neatly; leave a kind note inside one.",
           "Check back next week — restocking is a habit, not an event."],
          "45 minutes", "free"),
        D("Skill Gift",
          "Teach {who} one useful skill you have, in a single one-hour session.",
          {"who": ["a younger cousin", "a neighbor kid", "a coworker", "a grandparent"]},
          ["Pick one skill you can teach in an hour.",
           "Invite {who} with a specific time: 'Saturday at 2?'",
           "Teach slowly; let them do it, not watch you do it.",
           "End with a tiny certificate or high-five — ceremony matters."],
          "1 hour", "free"),
    ]
    big = [
        D("The Birthday They Would Skip",
          "Throw a small surprise celebration for {who}, who would otherwise let the day pass quietly.",
          {"who": ["a coworker far from family", "an elderly neighbor", "a friend going through a hard year"]},
          ["Quietly confirm the date with one insider.",
           "Gather 3-6 people and assign tiny jobs (cake, card, music).",
           "Keep the surprise kind, not startling — gentle reveal.",
           "Give them the card first; let the room applaud."],
          "one evening", "shared cost"),
        D("Community Clean Hour",
          "Organize a one-hour cleanup of {where} with whoever shows up.",
          {"where": ["your block", "the park", "the beach", "the schoolyard"]},
          ["Pick a visible spot and a one-hour window.",
           "Bring spare bags and gloves; invite with a simple flyer.",
           "Work the full hour together, then take a group photo.",
           "Thank everyone by name — volunteers return when thanked."],
          "2 hours", "bags and gloves"),
    ]
    return {"DEEDS": {"Quick Deeds": quick, "Planned Deeds": planned, "Big-Hearted Deeds": big}}


def _celeb_pools():
    T = {
        "Birthday": [
            "Happy birthday, {name}! Another year of you being exactly the wonderful {rel} you are — I hope this one brings you everything you quietly wished for.",
            "{name}, happy birthday! You make being a {rel} look easy and being a human look fun. Cake first, wishes second, regrets never.",
            "To {name} on your birthday: may your year be as generous as you are to everyone lucky enough to call you {rel}. Eat something delicious today.",
        ],
        "Graduation": [
            "{name}, you did it! All those late nights just turned into a diploma. Proud does not even cover it — your {rel} is cheering the loudest.",
            "Congratulations, graduate! {name}, watching you work for this as your {rel} has been the honor. Now go use that big brain on something wonderful.",
        ],
        "New Job": [
            "Congratulations on the new job, {name}! They have no idea how lucky they are. Your {rel} knew all along — go show them.",
            "{name}, first day nerves are just excitement in disguise. You earned this. Your {rel} believes in you completely.",
        ],
        "New Home": [
            "Happy new home, {name}! May the walls hold laughter, the kitchen hold good smells, and the {rel} visits be frequent.",
            "{name}, a new home is a new chapter with better lighting. Congratulations from your {rel} — I am bringing snacks to the housewarming.",
        ],
        "Wedding": [
            "{name}, wishing you a marriage as joyful as this wedding day. Your {rel} is so happy to celebrate two wonderful people becoming one team.",
            "Congratulations, {name}! Love chose well. As your {rel}, I promise excellent wedding cake opinions and lifelong cheering.",
        ],
        "New Baby": [
            "Welcome to the world, little one — and congratulations, {name}! Your {rel} is over the moon. Sleep now; the baby years fly.",
            "{name}, you are going to be an amazing parent. Your {rel} already knows it. Congratulations on the beautiful new arrival!",
        ],
        "Retirement": [
            "Happy retirement, {name}! You spent years making work better for everyone — now the calendar is yours. Your {rel} suggests naps first, adventures second.",
            "{name}, retirement looks good on you already. Congratulations from your {rel} — every Monday is now a Saturday.",
        ],
        "Thank You": [
            "{name}, thank you — truly. What you did meant more than you know, and your {rel} will not forget it.",
            "Just a note to say thank you, {name}. People like you are why people like me keep believing in people. Gratefully, your {rel}.",
        ],
        "Get Well": [
            "Get well soon, {name}! Rest up and let people fuss over you for once. Your {rel} is sending all the healing vibes and zero chores.",
            "Healing thoughts headed your way, {name}. Take it slow, take it easy — your {rel} has everything else covered.",
        ],
        "Congratulations": [
            "Congratulations, {name}! Big news deserves big cheers, and your {rel} is cheering the biggest. Savor this — you earned every bit.",
            "You did it, {name}! Congratulations from your {rel}, who is not even slightly surprised and enormously proud.",
        ],
    }
    return {"OCCASIONS": list(T.keys()), "TPL": T}


def _thank_pools():
    T = {
        "For a Gift": [
            "Dear {name}, thank you so much for the {thing}. It was thoughtful, perfect, and so very you. I thought of you the moment I opened it, and I have smiled about it every day since. With gratitude, your friend.",
            "{name}, the {thing} made my whole week. Thank you for knowing me so well — that is the real gift. I am lucky to have you in my life.",
        ],
        "For Help": [
            "Dear {name}, thank you for stepping in with {thing} when I needed it most. You made something hard feel manageable, and I will not forget it. I owe you one — and I mean that happily.",
            "{name}, your help with {thing} saved the day. Thank you for giving your time so generously. People like you make hard weeks survivable.",
        ],
        "For Hospitality": [
            "Dear {name}, thank you for the wonderful {thing}. Your home felt like a hug, the food was perfect, and the company was even better. Let me return the favor soon — my place, my cooking (be brave).",
            "{name}, thank you for {thing}. I left feeling rested, fed, and reminded how lucky I am to know you. Hospitality like yours is a gift.",
        ],
        "For Kind Words": [
            "Dear {name}, your {thing} arrived exactly when I needed to hear it. Thank you for saying the true thing kindly. I have kept your words close all week.",
            "{name}, thank you for {thing}. Encouragement from you carries weight, and it lifted me more than you know.",
        ],
        "For an Opportunity": [
            "Dear {name}, thank you for trusting me with {thing}. I will work hard to be worthy of the chance. Your belief in me means everything.",
            "{name}, thank you for opening the door to {thing}. Opportunities like this change trajectories, and I am deeply grateful you thought of me.",
        ],
    }
    things = {
        "For a Gift": ["beautiful book", "handmade scarf", "thoughtful card", "perfect kitchen gadget", "framed photo"],
        "For Help": ["the move", "the big project", "the car trouble", "the last-minute favor", "the tough week"],
        "For Hospitality": ["dinner party", "weekend stay", "holiday gathering", "cozy evening", "open-door welcome"],
        "For Kind Words": ["encouraging letter", "kind message", "heartfelt toast", "honest advice", "warm words"],
        "For an Opportunity": ["the interview", "the introduction", "the recommendation", "the new role", "the fresh start"],
    }
    out = {}
    for k, tpls in T.items():
        exp = []
        for t in tpls:
            for th in things[k][:2]:
                exp.append(t.replace("{thing}", th))
        out[k] = exp
    return {"TPL": out}


def _friend_pools():
    activities = [
        {"name": "The Two-Dollar Challenge",
         "desc": "Each person gets two dollars (or the local equivalent) and one hour to find the most delightful thing possible.",
         "steps": ["Hand everyone two dollars.", "Split up for exactly one hour.", "Return and present your find like a museum curator.", "Vote: most delightful wins eternal glory."],
         "materials": "two dollars per person", "time": "1.5 hours", "group": "2-6 friends"},
        {"name": "Cook-Off: Mystery Box",
         "desc": "Everyone draws three random ingredients and must cook something edible with them.",
         "steps": ["Fill a box with random pantry ingredients.", "Each cook draws three.", "45 minutes to create a dish.", "Everyone tastes; vote on taste AND bravery."],
         "materials": "pantry ingredients, basic kitchen", "time": "2 hours", "group": "2-5 friends"},
        {"name": "Memory Lane Walk",
         "desc": "Walk a route full of shared memories; at each stop someone tells the story.",
         "steps": ["Pick a route with 4-5 meaningful stops.", "At each stop, the person with the best memory tells it.", "Others add details they remember differently.", "End with dessert at the final stop."],
         "materials": "comfortable shoes", "time": "2-3 hours", "group": "2-8 friends"},
        {"name": "Skill Swap Night",
         "desc": "Everyone teaches the group one small skill in 15 minutes.",
         "steps": ["Each person picks one teachable skill.", "15 minutes to teach, 5 for questions.", "Rotate until everyone has taught.", "Vote for the skill you will actually keep using."],
         "materials": "whatever each skill needs", "time": "2 hours", "group": "3-6 friends"},
        {"name": "The Gratitude Circle",
         "desc": "Go around the circle; each person thanks the person to their left with one specific story.",
         "steps": ["Sit in a circle, phones away.", "Each person thanks the person on their left.", "The thanks must include one specific story.", "No deflecting — receive it graciously."],
         "materials": "a quiet room", "time": "45 minutes", "group": "3-10 friends"},
    ]
    questions = [
        "What is a small thing that always makes your day better?",
        "What skill do you wish you had learned as a kid?",
        "What is the best meal you have ever had, and who made it?",
        "If you could have dinner with anyone, living or not, who would it be?",
        "What is something you believed as a child that turned out to be gloriously wrong?",
        "What place have you never been that you dream about visiting?",
        "What is the kindest thing a stranger has ever done for you?",
        "What would you do with a completely free Saturday?",
        "What is a talent you have that most people do not know about?",
        "What movie or book changed how you see the world?",
        "What is your favorite memory from the past year?",
        "What advice would you give your ten-years-ago self?",
        "What is something you are looking forward to right now?",
        "What food could you eat every single day?",
        "What is the bravest thing you have ever done?",
        "What makes you laugh no matter how bad the day is?",
        "If you could master any instrument overnight, which one?",
        "What is a tradition from your family you want to keep?",
        "What is the most beautiful place you have ever seen?",
        "What small habit improved your life the most?",
    ]
    challenges = [
        {"name": "Seven-Day Compliment Streak",
         "desc": "Give one genuine, specific compliment to a different person every day for a week.",
         "steps": ["Pick your seven people (or find them as you go).", "Each compliment must be specific and true.", "Log each one with the date.", "On day seven, notice how people stand taller around you."],
         "window": "seven days"},
        {"name": "The Reconnection Week",
         "desc": "Contact one old friend you have lost touch with, every day for five days.",
         "steps": ["List five people you miss.", "Send each a real message — not just 'hey'.", "Mention one specific shared memory.", "Suggest one small concrete plan with at least one of them."],
         "window": "five days"},
        {"name": "Secret Supporter",
         "desc": "Do three anonymous kind acts for people you know this week.",
         "steps": ["Pick three people and three small acts.", "Do them without being seen.", "Leave zero evidence it was you.", "Enjoy the mystery — the secret is the point."],
         "window": "one week"},
    ]
    return {"ACTIVITIES": activities, "QUESTIONS": questions, "CHALLENGES": challenges}


def _family_pools():
    quiz = [
        {"q": "How many legs does a spider have?", "a": "Eight."},
        {"q": "What planet is known as the Red Planet?", "a": "Mars."},
        {"q": "How many days are in a leap year?", "a": "366."},
        {"q": "What is the largest ocean on Earth?", "a": "The Pacific Ocean."},
        {"q": "Which animal is the tallest in the world?", "a": "The giraffe."},
        {"q": "How many colors are in a rainbow?", "a": "Seven."},
        {"q": "What do you call a baby frog?", "a": "A tadpole."},
        {"q": "Which planet has beautiful rings around it?", "a": "Saturn."},
        {"q": "How many sides does a triangle have?", "a": "Three."},
        {"q": "What is the fastest land animal?", "a": "The cheetah."},
        {"q": "What gas do plants absorb from the air?", "a": "Carbon dioxide."},
        {"q": "How many minutes are in an hour?", "a": "Sixty."},
        {"q": "Which ocean is the Bermuda Triangle in?", "a": "The Atlantic Ocean."},
        {"q": "What is a group of wolves called?", "a": "A pack."},
        {"q": "How many strings does a violin have?", "a": "Four."},
        {"q": "What is the hardest natural substance on Earth?", "a": "Diamond."},
        {"q": "Which bird cannot fly but swims well?", "a": "The penguin."},
        {"q": "How many players are on a soccer team on the field?", "a": "Eleven."},
        {"q": "What is the capital of France?", "a": "Paris."},
        {"q": "What do caterpillars turn into?", "a": "Butterflies (or moths)."},
        {"q": "How many teeth does an adult human usually have?", "a": "Thirty-two."},
        {"q": "What is H2O commonly known as?", "a": "Water."},
        {"q": "Which continent is the Sahara Desert on?", "a": "Africa."},
        {"q": "What shape has five sides?", "a": "A pentagon."},
        {"q": "How many wheels does a tricycle have?", "a": "Three."},
        {"q": "What is the largest mammal in the world?", "a": "The blue whale."},
        {"q": "Which month has the fewest days?", "a": "February."},
        {"q": "What do you call frozen water?", "a": "Ice."},
        {"q": "How many cents are in a dollar?", "a": "One hundred."},
        {"q": "What animal says 'moo'?", "a": "A cow."},
        {"q": "What is the sun?", "a": "A star."},
        {"q": "How many seasons are there in a year?", "a": "Four."},
        {"q": "What color do you get mixing blue and yellow?", "a": "Green."},
        {"q": "Which animal is known as the king of the jungle?", "a": "The lion."},
        {"q": "How many hours are in a day?", "a": "Twenty-four."},
        {"q": "What do bees make?", "a": "Honey."},
        {"q": "What is the opposite of hot?", "a": "Cold."},
        {"q": "How many letters are in the English alphabet?", "a": "Twenty-six."},
        {"q": "What fruit keeps the doctor away, according to the saying?", "a": "An apple."},
        {"q": "Which animal hops and carries babies in a pouch?", "a": "A kangaroo."},
    ]
    hunt = ["something red", "something that makes noise", "something soft",
            "something older than you", "something that smells good",
            "something with wheels", "something you can wear",
            "something that grows", "something square", "something that reflects",
            "something with a button", "something that opens and closes",
            "something tiny", "something that floats", "something with stripes",
            "something you read", "something musical", "something from nature",
            "something blue", "something that keeps you warm", "something funny",
            "something with a handle", "something shiny", "something round"]
    charades = [
        {"w": "brushing teeth", "d": "Easy"}, {"w": "walking a dog", "d": "Easy"},
        {"w": "eating spaghetti", "d": "Easy"}, {"w": "playing basketball", "d": "Easy"},
        {"w": "a penguin waddling", "d": "Medium"}, {"w": "building a sandcastle", "d": "Medium"},
        {"w": "a robot dancing", "d": "Medium"}, {"w": "flying a kite", "d": "Medium"},
        {"w": "a popcorn kernel popping", "d": "Hard"}, {"w": "defusing a bomb (gently!)", "d": "Hard"},
        {"w": "a sloth crossing the road", "d": "Hard"}, {"w": "baking a cake in fast-forward", "d": "Hard"},
        {"w": "a cat chasing a laser pointer", "d": "Easy"}, {"w": "swimming upstream", "d": "Medium"},
        {"w": "a statue coming to life", "d": "Hard"}, {"w": "wrapping a present", "d": "Easy"},
    ]
    starters = [
        "On the morning of the big picnic, the family discovered the car would not start — and something was glowing in the garage.",
        "Grandma's old recipe box had one card nobody had ever dared to cook — until today.",
        "The power went out during the storm, and that is when the knocking started — three knocks, then giggling.",
        "A mysterious package arrived with no return address, labeled: OPEN TOGETHER AFTER DINNER.",
        "The new puppy dug up something shiny in the backyard that hummed when you held it.",
    ]
    twists = ["A talking parrot lands on the windowsill with urgent news.",
              "Someone's phone starts playing music nobody recognizes — and it is coming from inside the walls.",
              "A long-lost relative knocks on the door holding a pie.",
              "Everything suddenly goes silent — even the birds.",
              "A map falls out of a book, marked with an X in your own neighborhood.",
              "The youngest person present suddenly knows exactly what to do.",
              "It starts raining — indoors. Just a little."]
    return {"QUIZ": quiz, "HUNT": hunt, "CHARADES": charades,
            "STARTERS": starters, "TWISTS": twists}


def _adv_pools():
    def A(name, mission, venue, crew, roles, checklist, debrief):
        return {"name": name, "mission": mission, "venue": venue, "crew": crew,
                "roles": roles, "checklist": checklist, "debrief": debrief}
    day = [
        A("The Great Thrift Hunt",
          "Each team gets $10 and one hour in a thrift store to assemble the most legendary outfit.",
          "a local thrift store", "3-8 people",
          ["Team Captain (keeps time)", "Stylist (final say on outfits)", "Photographer (documents everything)", "Treasurer (holds the $10)"],
          ["Set a strict $10 budget per team", "One hour on the clock — no extensions", "Every team member must wear their outfit out of the store", "Group runway show in the parking lot", "Vote: boldest look wins"],
          ["What was the best find?", "Who committed hardest to the bit?", "Would you actually wear any of it again?"]),
        A("Park Games Decathlon",
          "Ten silly mini-games across the park; the crew with the most points takes the crown.",
          "a big public park", "4-12 people",
          ["Referee (explains rules, settles disputes)", "Scorekeeper", "Hype Person (mandatory cheering)", "Water Bearer"],
          ["Frisbee accuracy toss", "Three-legged race", "Sack-style hop race (pillowcases work)", "Water balloon toss (no filling stations? use soft balls)", "Best team cheer contest", "Tally scores loudly after each event"],
          ["Which event was secretly the hardest?", "Best moment of the day?", "Rematch — yes or yes?"]),
        A("Neighborhood Photo Safari",
          "Capture the alphabet: one photo for each letter A-Z, found in the wild of your neighborhood.",
          "your neighborhood", "2-6 people",
          ["Navigator (plans the route)", "Spotter (eagle eyes)", "Photographer", "List Keeper (tracks letters found)"],
          ["No driving — feet or bikes only", "Each letter needs a real found object (A = apple tree, B = bicycle...)", "Bonus for the funniest Q, X, Z", "Assemble the alphabet collage at the end", "Share it with someone who will appreciate it"],
          ["Which letter was the hardest?", "What did you notice that you had never seen before?"]),
    ]
    evening = [
        A("Sunset Picnic and Stories",
          "Pack dinner, claim the best sunset spot, and trade stories until the stars come out.",
          "a hill, beach, or rooftop with a western view", "2-8 people",
          ["Quartermaster (packs food and blankets)", "Scout (claims the spot early)", "Storyteller (starts the first story)", "Stargazer (knows one constellation)"],
          ["Arrive 90 minutes before sunset", "Everyone brings one dish to share", "Phones away once the sun touches the horizon", "Each person tells one true story", "Stay for the first stars"],
          ["Whose story surprised you most?", "What are you grateful for tonight?"]),
        A("Living-Room Concert Night",
          "Everyone performs something — song, poem, comedy bit, magic trick. Applause is mandatory.",
          "someone's living room", "3-10 people",
          ["MC (introduces each act with flair)", "Stage Manager (arranges the 'stage')", "Hype Crew (front row, loudest claps)", "Snack Captain"],
          ["Every person performs at least once", "Acts under 5 minutes", "No booing — ever", "Encore for the bravest act", "Group finale: everyone sings something together"],
          ["Who surprised you?", "What should be a tradition?"]),
    ]
    weekend = [
        A("The Two-Town Tour",
          "Visit two nearby towns you have never explored; collect one souvenir and one story from each.",
          "two neighboring towns", "2-6 people",
          ["Driver/Navigator", "Food Scout (finds the local spot)", "Historian (reads one plaque aloud per town)", "Souvenir Keeper"],
          ["Pick towns within an hour's drive", "Eat where the locals eat", "Find the town's oddest landmark", "Buy one small souvenir per town", "Learn one fact per town to retell"],
          ["Which town would you move to?", "Best bite of the weekend?"]),
        A("Campfire Tales Weekend",
          "One night outdoors (or backyard-camping) built around stories, stars, and s'mores.",
          "a campsite or backyard", "2-8 people",
          ["Fire Tender (safety first, always)", "S'mores Engineer", "Story Keeper (starts the tale chain)", "Dawn Patrol (handles breakfast)"],
          ["Check fire rules and weather first", "Set up camp before dark", "Everyone contributes one story", "Lights out when the fire is fully out", "Leave the site cleaner than you found it"],
          ["Best story of the night?", "What sound will you remember?"]),
    ]
    return {"ADV": {"Day Adventures": day, "Evening Adventures": evening,
                    "Weekend Adventures": weekend}}


GEN_SPECS = {
    "palindrome": (PAL_BODY, _pal_pools, "palindrome playground record"),
    "good-deed": (DEED_BODY, _deed_pools, "good deed record"),
    "celebration": (CELEB_BODY, _celeb_pools, "celebration message record"),
    "thank-you": (THANK_BODY, _thank_pools, "thank-you note record"),
    "friendship": (FRIEND_BODY, _friend_pools, "friendship builder record"),
    "family-game": (FAMILY_BODY, _family_pools, "family game record"),
    "social-adventure": (ADV_BODY, _adv_pools, "social adventure record"),
}


def render(kind, name, slug, genver, prefix, src, record_kind):
    body, pool_fn, _rk = GEN_SPECS[kind]
    pools = pool_fn()
    t = HEADER + body + FOOTER
    subs = {
        "@@NAME@@": name, "@@GENVER@@": _js_str(genver),
        "@@PREFIX@@": _js_str(prefix), "@@SRC@@": _js_str(src),
        "@@RECORD_KIND@@": _js_str(record_kind),
        "@@SLUG@@": _js_str(slug),
    }
    for k, v in pools.items():
        subs["@@%s@@" % k] = json.dumps(v, ensure_ascii=False)
    for k, v in subs.items():
        t = t.replace(k, v)
    import re
    leftover = re.findall(r"@@[A-Z_]+@@", t)
    assert not leftover, "unreplaced tokens: %s" % leftover[:5]
    return t


def write_real_generators(cfg, kind):
    """Overwrite both editions' gen JS with the real generator; test them."""
    import tempfile
    for edition, slug, prefix, src in (
        ("pub", cfg["slug"], cfg["prefix_pub"], "public-harvest"),
        ("sig", cfg["slug"] + "-signature", cfg["prefix_sig"], "signature"),
    ):
        name = cfg["name_pub"] if edition == "pub" else cfg["name_sig"]
        genver = "jahdb-%s-1.0" % slug
        js = render(kind, name, slug, genver, prefix, src, cfg["record_kind"])
        gpath = os.path.join(REPO, "db", slug, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(js)
        p = subprocess.run(["node", "--check", gpath], capture_output=True, text=True)
        assert p.returncode == 0, "node --check failed %s: %s" % (slug, p.stderr[:300])
        node_test = (
            "const g=require(%s);"
            "let n=0;"
            "for(const s of [7,42,3001]){"
            "  const r=g.generate(s,{});"
            "  const v=g.validate(r);"
            "  if(!v.ok) throw new Error('validate failed '+JSON.stringify(v.errors));"
            "  if(!r.demo||!r.demo.program) throw new Error('no demo');"
            "  require('fs').writeFileSync('/tmp/_rgdemo_'+s+'.py', r.demo.program);"
            "  n++;}"
            "console.log('GEN_OK '+n);"
        ) % json.dumps(gpath)
        p = subprocess.run(["node", "-e", node_test], capture_output=True, text=True)
        assert p.returncode == 0 and "GEN_OK 3" in p.stdout, \
            "gen test failed %s: %s" % (slug, p.stderr[:300])
        for s in (7, 42, 3001):
            with open("/tmp/_rgdemo_%d.py" % s, encoding="utf-8") as f:
                prog = f.read()
            with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as tf:
                tf.write(prog)
                tpath = tf.name
            try:
                pr = subprocess.run([sys.executable, tpath], capture_output=True,
                                    text=True, timeout=30)
                assert pr.returncode == 0 and pr.stdout.strip(), \
                    "demo failed %s seed %d: %s" % (slug, s, pr.stderr[:200])
            finally:
                try:
                    os.unlink(tpath)
                except OSError:
                    pass
        print("real generator OK:", gpath)
